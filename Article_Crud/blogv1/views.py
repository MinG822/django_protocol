from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'blogv1/index.html', context)


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(
            title=title,
            content=content
        )
        return redirect('blogv1:index')
    else:
        return render(request, 'blogv1/create.html')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'blogv1/detail.html', context)

def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect('blogv1:index')

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        context = {
            'article' : article
        }
        return render(request, 'blogv1/detail.html', context)
    else:
        context = {
            'article' : article
        }
        return render(request, 'blogv1/update.html', context)