from django import forms
from .models import PaUploadedFile

class PaFileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file', 'category']  # Користувач не вказується, він буде прив'язаний у views.py
