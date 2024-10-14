from django.urls import path

from .views import filter_files_by_category, main, upload

app_name = 'pa_file'

urlpatterns = [
    path('', main, name='home'),
    path('add/', upload, name='create'),
    path('<str:category>/', filter_files_by_category, name='type'),
]
