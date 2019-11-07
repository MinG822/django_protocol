from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/update/', views.update, name="update"),
    path('<int:article_pk>/like/', views.like, name='like'),
]