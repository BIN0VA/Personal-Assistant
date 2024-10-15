from django.forms import CharField, ModelForm, Textarea, TextInput

from pa_core.forms import FormHelper
from .models import Note


class NoteForm(ModelForm):
    name = CharField(
        max_length=50,
        min_length=3,
        required=True,
        widget=TextInput(FormHelper.attributes(
            'name',
            'Find a birthday present for my best friend',
        )),
    )

    description = CharField(
        max_length=150,
        required=False,
        widget=Textarea(FormHelper.attributes(
            'description',
            'Consider getting a special book, a personalized keepsake, or '
            'tickets to a game of his favorite team. Think about what she '
            'loves and what would make his day memorable.',
        )),
    )

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super().__init__(*args, **kwargs)

        self.fields['description'].widget.attrs['rows'] = 3

    class Meta:
        model = Note
        fields = ('name', 'description')
        exclude = ('tags',)


class NoteDoneForm(ModelForm):
    class Meta:
        model = Note
        fields = ('done',)
