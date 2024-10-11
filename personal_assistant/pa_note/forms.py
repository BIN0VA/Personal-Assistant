from django.forms import ModelForm

from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'description']


class NoteDoneForm(ModelForm):
    class Meta:
        model = Note
        fields = ['done']
