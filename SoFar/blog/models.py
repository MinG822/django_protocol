from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'article_pk':self.pk})

class Comment(models.Model):
    content = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)
    
    def __str__(self):
        return self.content
    