from django.forms import ModelForm, CharField, TextInput

from pa_core.forms import FormHelper
from .models import Tag


class TagForm(ModelForm):

    name = CharField(
        min_length=3,
        max_length=25,
        required=True,
        widget=TextInput(FormHelper.attributes(
            'name',
            'Shopping, Personal, Work, Urgent, Ideas, etc.',
        )),
    )

    class Meta:
        model = Tag
        fields = ('name',)
