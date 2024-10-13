from django.forms import ModelForm, CheckboxSelectMultiple

from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'description', 'done', 'tags']  
        widgets = {
            'tags': CheckboxSelectMultiple(),  
        }


class NoteDoneForm(ModelForm):
    class Meta:
        model = Note
        fields = ['done']
