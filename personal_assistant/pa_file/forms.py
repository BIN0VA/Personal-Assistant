from django.forms import ModelForm

from .models import File


class PaFileUploadForm(ModelForm):
    class Meta:
        model = File

        # Користувач не вказується, він буде прив'язаний у views.py
        fields = ('file', 'category')
