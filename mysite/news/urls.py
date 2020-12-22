from django.urls import path
from .views import index, category


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:pk>/', category, name='category')
]