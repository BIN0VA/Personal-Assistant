from django.forms import (
    FileField,
    FileInput,
    ModelForm,
    MultipleChoiceField,
    RadioSelect,
)

from pa_core.forms import FormHelper
from .models import File


class PaRadioSelect(RadioSelect):
    template_name = 'pa_file/radios.html'


class PaFileUploadForm(ModelForm):
    file = FileField(widget=FileInput(FormHelper.attributes('file')))

    category = MultipleChoiceField(
        choices=File.CATEGORIES,
        widget=PaRadioSelect({'class': 'btn-group'}),
    )

    class Meta:
        model = File

        # Користувач не вказується, він буде прив'язаний у views.py
        fields = ('file', 'category')
