from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('contacts/', views.main, name='main'),
    path('contacts/add_contact/', views.add_contact, name='add_contact'),
    path('contacts/detail/<int:contact_id>', views.detail, name='detail'),
    path('delete/<int:contact_id>', views.delete_contact, name='delete'),
]