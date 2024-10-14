from django.urls import path

from .views import delete, main


app_name = 'pa_tag'

urlpatterns = [
    path('', main, name='home'),
    path('<int:tag_id>/', delete, name='delete'),
]
