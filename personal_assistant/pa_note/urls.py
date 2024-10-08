from django.urls import path
from . import views


app_name = 'pa_note'

urlpatterns = [
    path('', views.note, name='note'),
    path('add/', views.NoteCreateView.as_view(), name='add_note'),
    path('delete/<int:pk>/', views.NoteDeleteView.as_view(), name='delete_note'),
    path('edit/<int:pk>/', views.NoteUpdateView.as_view(), name='edit_note'),

]
