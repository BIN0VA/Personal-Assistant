from django.urls import path

from .views import display_news

urlpatterns = [
    path('', display_news, name='news_summary'),
]
