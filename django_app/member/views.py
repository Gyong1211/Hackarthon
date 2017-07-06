from django.contrib.auth import login as django_login, \
    logout as django_logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from member.forms import LoginForm, SignupForm


def main(request):
    if request.user.is_authenticated():
        return redirect('attendance:attendance_create')
    return render(request, 'member/main.html')


def login(request):

    print(request)

    if request.method == 'POST':
        print('post: {}'.format(request))
        form = LoginForm(data=request.POST)
        print(form)
        print(form)

        if form.is_valid():
            user = form.cleaned_data['user']
            django_login(request, user)
            return redirect('attendance:attendance_create')

    else:
        print('get: {}'.format(request))
        if request.user.is_authenticated:
            return redirect('attendance:attendance_create')
    form = LoginForm()
    context = {
        'form': form,

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
        'form': form,
    }
    return render(request, 'member/signup.html', context)
