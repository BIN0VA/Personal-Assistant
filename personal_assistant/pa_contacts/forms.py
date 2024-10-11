from django.forms import ModelForm, CharField, EmailField, TextInput, DateField, DateInput
from django.core.exceptions import ValidationError
from phonenumbers import parse, is_valid_number, NumberParseException, format_number, PhoneNumberFormat

from .models import Contact

import datetime
import re


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
        max_length=20, 
        required=True, 
        widget=TextInput(attrs={'class': 'form-control'})
    )
    email = EmailField(
        min_length=5, 
        max_length=50, 
        required=False, 
        widget=TextInput(attrs={
            'class': 'form-control',
            'type': 'email',  
            'id': 'email', 
            'name': 'email',
        })
    )
    birthday = DateField(
        required=False, 
        widget=DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    class Meta:
        model = Contact
        fields = ['name', 'address', 'phone', 'email', 'birthday']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.errors.get(field):
                self.fields[field].widget.attrs['class'] += ' is-invalid'
            else:
                self.fields[field].widget.attrs['class'] += ' form-control'

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if phone:
            phone = re.sub(r'(?<!^)\D+', '', phone)

            try:
                if phone.startswith('+'):
                    parsed_phone = parse(phone, None)  
                else:
                    parsed_phone = parse(phone, 'UA')

                if not is_valid_number(parsed_phone):
                    raise ValidationError('Please enter a valid phone number.')


                formatted_phone = format_number(parsed_phone, PhoneNumberFormat.E164)
                return formatted_phone

            except NumberParseException as e:
                raise ValidationError('Please enter a valid phone number.')

        return phone
