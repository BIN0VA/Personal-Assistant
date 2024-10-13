from django.urls import path

from .views import home, search

app_name = 'pa_core'

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
]
