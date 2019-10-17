from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:article_pk>', views.detail, name="detail"),
    path('<int:article_pk>/delete', views.delete, name="delete"),
    path('<int:article_pk>/update/', views.update, name="update"),
    path('<int:article_pk>/comment_create', views.comment_create, name="comment_create"),
    path('<int:comment_pk>/comment_delete', views.comment_delete, name="comment_delete"),
    path('<int:article_pk>/<int:comment_pk>/comment_update', views.comment_update, name="comment_update"),
]
