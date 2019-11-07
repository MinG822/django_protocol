from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    # 꼭패스워드여야한다.
    path('password/', views.change_password, name='change_password'),
    path('follow/<int:person_pk>', views.follow, name='follow'),
]