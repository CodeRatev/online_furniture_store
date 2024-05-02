from django.shortcuts import render

# Create your views here.

def login(request):
    context = {
        'title': '12 стульев - Авторизация'
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': '12 стульев - Регистрация'
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': '12 стульев - Кабинет'
    }
    return render(request, 'users/profile.html', context)

def  logout(request):
    ...