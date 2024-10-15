from django.urls import path

from .views import (
    CreateView,
    DeleteView,
    done,
    note,
    UpdateView,
)

app_name = 'pa_note'

urlpatterns = [
    path('', note, name='home'),
    path('add/', CreateView.as_view(), name='create'),
    path('<int:note_id>/', UpdateView.as_view(), name='edit'),
    path('<int:note_id>/done/', done, name='done'),
    path('<int:note_id>/delete/', DeleteView.as_view(), name='delete'),
]
