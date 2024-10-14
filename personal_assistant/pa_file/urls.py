from django.urls import path

from .views import main, upload

app_name = 'pa_file'

urlpatterns = [
    path('add/', upload, name='create'),
    path('<str:category>/', main, name='category'),
    path('', main, name='home'),
]
