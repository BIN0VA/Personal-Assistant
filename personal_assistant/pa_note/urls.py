from django.urls import path

from .views import CreateView, DeleteView, DoneUpdateView, note, UpdateView

app_name = 'pa_note'

urlpatterns = [
    path('', note, name='note'),
    path('add/', CreateView.as_view(), name='add_note'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete_note'),
    path('edit/<int:pk>/', UpdateView.as_view(), name='edit_note'),
    path('note/<int:pk>/done/', DoneUpdateView.as_view(), name='done_note'),
]
