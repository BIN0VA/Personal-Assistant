# news_app/urls.py

from django.urls import path
from .views import display_news
urlpatterns = [
    path('',display_news, name='news_summary'),  # Головний маршрут для новин
    
]
