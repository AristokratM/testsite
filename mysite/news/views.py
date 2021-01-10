from django.http import HttpResponse
from django.shortcuts import render
from .models import News, Category

# Create your views here.


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context)


def category(request, pk):
    news = News.objects.filter(category__id=pk)
    category = Category.objects.get(pk=pk)
    context = {
        'news': news,
        'title': 'Список новостей',
        'category': category
    }
    return render(request, 'news/category.html', context)


def view_news(request, pk):
    news_item = News.objects.get(pk=pk)
    return render(request, 'news/view_news.html', {'news_item': news_item})

