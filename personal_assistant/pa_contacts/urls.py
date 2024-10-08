from django.urls import path

from .views import main, create, delete

app_name = 'pa_contacts'

urlpatterns = [
    path('', main, name='main'),
    path('add/', create, name='add_contact'),
    path('<int:contact_id>/delete', delete, name='delete'),
]
