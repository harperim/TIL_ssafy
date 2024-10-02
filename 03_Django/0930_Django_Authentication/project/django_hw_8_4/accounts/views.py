from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import User
# Create your views here.

def index(request):
    # 디폴트값은 오름차순, 게시판은 최신글부터 띄워야하므로 내림차순으로 반환
    # 내림차순은 앞에 -만 붙이기
    # persons = User.objects.order_by(-pk)  
    persons = User.objects.all()
    context = {
        'persons': persons,
    }  
    return render(request, 'accounts/index.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # form.save() 대신 로그인 처리
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()  # Form, ModelForm
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:index')
