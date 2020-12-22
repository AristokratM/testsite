from django.http import HttpResponse
from django.shortcuts import render
from .models import News, Category

# Create your views here.


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories
    }
    return render(request, 'news/index.html', context)


def category(request, pk):
    news = News.objects.filter(category__id=pk)
    categories = Category.objects.all()
    category = Category.objects.get(pk=pk)
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,
        'category': category
    }
    return render(request, 'news/category.html', context)