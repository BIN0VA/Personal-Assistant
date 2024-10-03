from django.urls import path

from .views import home

app_name = 'pa_core'

urlpatterns = [
    path('', home, name='home'),
]
