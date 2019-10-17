from django.shortcuts import render, redirect
from .models import Article, Comment
# Create your views here.

# 인덱스 함수
def index(request):
    articles = Article.objects.all()
    context = {
        "articles" : articles,
    }
    if request.session.get("comment_pk"):
        del request.session["comment_pk"]
    return render(request, 'board/index.html', context)

# 게시글 작성 함수
def create(request):
    if request.method == "POST":
        article = Article.objects.create(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
        )
        return redirect('board:detail', article.pk)
    else:
        return render(request, 'board/create.html')

# 게시글 상세보기 함수
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = Comment.objects.filter(article=article)
    context = {
            "article" : article,
            "comments" : comments
        }
    if request.session.get("comment_pk"):
        context["comment_pk"] = request.session.get("comment_pk")
    return render(request, 'board/detail.html', context)

# 게시글 수정하기 함수
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
            "article" : article
        }
    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect('board:detail', article_pk)
    else:
        return render(request, 'board/update.html', context)

# 게시글 삭제하기 함수
def delete(request, article_pk):
    Article.objects.get(pk=article_pk).delete()
    return redirect('board:index')

# 게시글에 달릴 댓글 작성하기 함수
def comment_create(request, article_pk):
    comment = Comment.objects.create(
        content = request.POST.get('content'),
        article = Article.objects.get(pk=article_pk)
    )
    return redirect('board:detail', article_pk)

# 게시글에 달린 댓글 삭제하기 함수
# urls에서 파라미터가 두 개이기 때문에 article_pk와 comment_pk 가 모두 필요하다.
def comment_delete(request, article_pk, comment_pk):
    Comment.objects.get(pk=comment_pk).delete()
    return redirect('board:detail', article_pk)

# 게시글에 달린 댓글 수정하기 함수
def comment_update(request, article_pk, comment_pk):
    if request.method == "POST":
        # Comment.objects.filter(pk=comment_pk).update(content=request.POST.get("updatedcontent"))
        comment = Comment.objects.get(pk=comment_pk)
        comment.content = request.POST.get("updatedcontent")
        comment.article = Article.objects.get(pk=article_pk)
        comment.save()
        del request.session["comment_pk"]
        return redirect('board:detail', article_pk)
    else:
        request.session["comment_pk"] = comment_pk
        return detail(request, article_pk)

