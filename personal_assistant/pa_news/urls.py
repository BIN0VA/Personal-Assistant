from django.urls import path

from .views import bank

app_name = 'pa_news'

urlpatterns = [
    path('', bank, name='bank'),
]
