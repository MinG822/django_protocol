from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    context = {
        "articles" : Article.objects.all()
    }
    if request.session.get('comment_pk'):
        del request.session["comment_pk"]
    return render(request, 'blog/index.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    context = {
        "form" : ArticleForm()
    }
    return render(request, 'blog/create.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    form = CommentForm()
    context = {
        "article" : article,
        "comments" : comments,
        "form" : form,
    }
    if request.session.get("comment_pk"):
        comment_pk = request.session.get('comment_pk')
        context["comment_pk"] = comment_pk
        context["updateform"] = CommentForm(instance=Comment.objects.get(pk=comment_pk))
    return render(request, 'blog/detail.html', context)

@require_POST
def delete(request, article_pk):
    if request.method == "POST":
        get_object_or_404(Article, pk=article_pk).delete()
    return redirect('blog:index')

# 중요
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect(article)
    form = ArticleForm(instance=article)
    context = {
        "article" : article,
        "form" : form,
    }
    return render(request, 'blog/update.html', context)

@require_POST
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.article=article
            new_comment = form.save()
    return redirect(article)

@require_POST
def comment_delete(request, comment_pk):
    if request.method == "POST":
        comment = get_object_or_404(Comment, pk=comment_pk)
        article = comment.article
        comment.delete()
    return redirect(article)

def comment_update(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            del request.session["comment_pk"]
            return redirect(article)
    updateform = CommentForm(instance=comment)
    request.session["comment_pk"] = comment_pk
    return detail(request, article_pk)



