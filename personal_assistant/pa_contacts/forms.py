from datetime import datetime
from re import sub

from django.forms import ModelForm, CharField, EmailField, TextInput, \
    DateField, DateInput
from django.core.exceptions import ValidationError
from phonenumbers import parse, is_valid_number, NumberParseException, \
    format_number, PhoneNumberFormat

from .models import Contact


PHONE = '+380776665544'


class ContactsForm(ModelForm):
    current_year = datetime.now().year

    name = CharField(
        min_length=1,
        max_length=50,
        required=True,
        widget=TextInput({'class': 'form-control'}),
    )

    address = CharField(
        min_length=10,
        max_length=150,
        required=False,
        widget=TextInput({'class': 'form-control'}),
    )

    phone = CharField(
        min_length=10,
        max_length=20,
        required=True,
        widget=TextInput({'class': 'form-control', 'placeholder': PHONE}),
    )

    email = EmailField(
        min_length=5,
        max_length=50,
        required=False,
        widget=TextInput({
            'class': 'form-control',
            'type': 'email',
            'id': 'email',
            'name': 'email',
            'placeholder': 'example@example.com',
        }),
    )

    birthday = DateField(
        required=False,
        widget=DateInput({'class': 'form-control', 'type': 'date'})
    )

    class Meta:
        model = Contact
        fields = ('name', 'address', 'phone', 'email', 'birthday')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)

        super().__init__(*args, **kwargs)

        for field in self.fields:
            if self.errors.get(field):
                self.fields[field].widget.attrs['class'] += ' is-invalid'
            else:
                self.fields[field].widget.attrs['class'] += ' form-control'

    def clean_phone(self):
        if phone := self.cleaned_data.get('phone'):
            phone = sub(r'(?<!^)\D+', '', phone)

            incorrect = ValidationError(
                'Please enter your phone number in the international format '
                f'(e.g., {PHONE}).',
            )

            try:
                if (
                    Contact.objects
                    .filter(user=self.user, phone=phone)
                    .exclude(id=self.instance.id if self.instance else None)
                    .exists()
                ):
                    raise ValidationError(
                        'A contact with this phone number already exists.',
                    )

                parsed = parse(phone, None if phone.startswith('+') else 'UA')

                if not is_valid_number(parsed):
                    raise incorrect

                return format_number(parsed, PhoneNumberFormat.E164)

            except NumberParseException:
                raise incorrect

        return phone

    def clean_email(self):
        if (
            (email := self.cleaned_data.get('email')) and

            Contact.objects
            .filter(user=self.user, email=email)
            .exclude(id=self.instance.id if self.instance else None)
            .exists()
        ):
            raise ValidationError('A contact with this e-mail already exists.')

        return email
