from django.urls import path

from .views import tags, delete


app_name = 'pa_tag'

urlpatterns = [
    path('', tags, name='tags'),
    path('delete/<int:tag_id>/', delete, name='delete'),
]