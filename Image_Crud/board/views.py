from django.shortcuts import render, redirect
from .models import Article
# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'board/index.html', context)

def create(request):
    if request.method == "POST":
        Article.objects.create(
            title = request.POST.get("title"),
            content = request.POST.get('content'),
            Image = request.FILES.get("image")
        )
        return redirect('board:index')
    else:
        return render(request, 'board/create.html')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'board/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.Image = request.FILES.get("image")
        article.save()
        return redirect('board:detail', pk)
    else:
        context = {
            "article" : article
        }
        return render(request, 'board/update.html', context)

def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect('board:index')
