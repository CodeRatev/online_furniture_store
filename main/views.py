from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):
    
    context = {
        'title': '12 стульев - Главная',
        'content': "Магазин мебели 12 стульев",
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': '12 стульев - О нас',
        'content': "О нас",
    }
    return render(request, 'main/about.html', context)
