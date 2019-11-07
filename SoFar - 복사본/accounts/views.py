from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.

# 회원가입
def signup(request):
    if request.user.is_authenticated:
        return redirect('blog:index')

    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/auth_form.html', context)

def login(request):
    # 만약 로그인되어있으면 다시 index페이지로
    if request.user.is_authenticated:
        return redirect('blog:index')
    if request.method == 'POST':
        # UserCreationForm과 필수인자가 다름
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인, db와 비교검증
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'blog:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/auth_form.html', context)

@login_required
def logout(request):
    # 세션을 지우기
    auth_logout(request)
    return redirect('blog:index')

@require_POST
def delete(request):
    #DB에서 user를 삭제하기
    request.user.delete()
    return redirect('blog:index')

@login_required
def update(request):
    #회원정보 수정
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        # 편집화면을 보여줌
        form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/auth_form.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # session auth hash 가 변경되며 로그아웃되어버리거나 에러가 뜨기 때문에 
            update_session_auth_hash(request, form.user)
            return redirect('blog:index')
    
    form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/auth_form.html', context)

def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

def follow(request, person_pk):
    person = get_object_or_404(get_user_model(), pk=person_pk)
    user = request.user

    if person.followers.filter(pk=user.pk).exists():
        person.followers.remove(user)
    else:
        person.followers.add(user)
    
    return redirect('profile', person.username)