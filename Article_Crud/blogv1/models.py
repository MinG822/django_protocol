from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 최근 글 순서로 정렬하기
    # class Meta(modles.Meta):
        
