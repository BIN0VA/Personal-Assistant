from django.urls import path

from .views import bank, UpdateView

app_name = 'pa_news'

urlpatterns = [
    path('', bank, name='bank'),
    path('update/', UpdateView.as_view(), name='update'),
]
