from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': '12 сутльев - Главная',
        'content': "Магазин мебели 12 стульев"
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': '12 сутльев - О нас',
        'content': "О нас",
        'text_on_page': "Это новый текст"
    }
    return render(request, 'main/about.html', context)
