from django import forms
from .models import PaUploadedFile

class PaFileUploadForm(forms.ModelForm):
    class Meta:
        model = PaUploadedFile
        fields = ['file', 'category']
