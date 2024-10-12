from django.urls import path

from .views import bank, recent

app_name = 'pa_news'

urlpatterns = [
    path('', recent, name='recent'),
    path('bank/', bank, name='bank'),
]
