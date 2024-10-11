from django.urls import path

from . import views

app_name = 'pa_note'

urlpatterns = [
    path('', views.note, name='note'),
    path('add/', views.CreateView.as_view(), name='add_note'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete_note'),
    path('edit/<int:pk>/', views.UpdateView.as_view(), name='edit_note'),
    path('note/<int:pk>/done/', views.DoneUpdateView.as_view(), name='done_note'),
    path('search/', views.notes_search, name='search'),
]
