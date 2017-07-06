from django.contrib.auth import login as django_login,\
    logout as django_logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from member.forms import LoginForm, SignupForm


def main(request):
    return render(request, 'member/main.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            django_login(request, user)
            return redirect('member:main')

        else:
            return HttpResponse('Login credential is invalid')
    else:
        if request.user.is_authenticated:
            return redirect('member:main')
        form = LoginForm()
        context = {
            'form':form,

        }
        return render(request, 'member/login.html', context)

def logout(request):
    django_logout(request)
    return redirect('member:main')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.create_user()
            django_login(request, user)
            return redirect('member:main')
    else:
        form = SignupForm()
    context = {
        'form':form,
    }
    return render(request, 'member/signup.html', context)