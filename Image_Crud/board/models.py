from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    Image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)