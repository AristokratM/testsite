from django.urls import path
from .views import index, category, view_news


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:pk>/', category, name='category'),
    path('news/<int:pk>/', view_news, name="view_news"),

]