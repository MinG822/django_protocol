from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        ordering = ('-pk',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})