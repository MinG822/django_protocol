from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'blog/index.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article.objects.create(**form.cleaned_data)
            return redirect(article)
    else:
        form = ArticleForm()
        context = {
            'form' : form
        }
        return render(request, 'blog/create.html', context)

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        "article" : article
    }
    return render(request, 'blog/detail.html', context)

@ require_POST
def delete(request, pk):
    if request.method == "POST":
        Article.objects.get(pk=pk).delete()
        return redirect("blog:index")
    else:
        return redirect("blog:index")

def update(request, pk):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            Article.objects.filter(pk=pk).update(**form.cleaned_data)
            return redirect(Article.objects.get(pk=pk))
    # request.method가 POST가 아닐때와 valid하지 않을 때
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(initial={"title" : article.title, "content" : article.content })
    context = {
        "form" : form,
        'article' : article,
    }
    return render(request, 'blog/update.html', context)