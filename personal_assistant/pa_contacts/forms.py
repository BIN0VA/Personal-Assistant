from django.forms import ModelForm, CharField, TextInput, DateField, DateInput

from .models import Contact

import datetime

class ContactsForm(ModelForm):
    current_year = datetime.datetime.now().year
    name = CharField(
        min_length=1, 
        max_length=50, 
        required=True, 
        widget=TextInput(attrs={'class': 'form-control'})
    )
    address = CharField(
        min_length=10, 
        max_length=150, 
        required=False, 
        widget=TextInput(attrs={'class': 'form-control'})
    )
    phone = CharField(
        min_length=10, 
        max_length=12, 
        required=True, 
        widget=TextInput(attrs={'class': 'form-control'})
    )
    email = CharField(
        min_length=5, 
        max_length=50, 
        required=False, 
        widget=TextInput(attrs={'class': 'form-control'})
    )
    birthday = DateField(
        required=False, 
        widget=DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    class Meta:
        model = Contact
        fields = ['name', 'address', 'phone', 'email', 'birthday']
        