from django.urls import path

from .views import main, add_tag, delete

app_name = 'pa_tags'

urlpatterns = [
    path('', main, name='main'),
    path('add_tag', add_tag, name='add_tag'),
    path('<int:tag_id>delete', delete, name='delete'),
]