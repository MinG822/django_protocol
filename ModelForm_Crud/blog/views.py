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
            form.save()
            return redirect('blog:index')
    context={
        "form" : ArticleForm(),
    }
    return render(request, 'blog/create.html', context)

def detail(request, pk):
    context = {
        "article" : get_object_or_404(Article, pk=pk)
    } 
    return render(request, 'blog/detail.html', context)

@require_POST
def delete(request, pk):
    if request.method == "POST":
        Article.objects.get(pk=pk).delete()
    return redirect('blog:index')

# 주의
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect(article)
    
    form = ArticleForm(instance=article)
    context = {
        "form" : form,
        "article" : article,
    }
    return render(request, 'blog/update.html', context)

