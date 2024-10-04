from django.forms import ModelForm, CharField, TextInput, DateField, SelectDateWidget
from .models import Contact
import datetime

class ContactsForm(ModelForm):
    current_year = datetime.datetime.now().year
    name = CharField(min_length=1, max_length=50, required=True, widget=TextInput())
    address = CharField(min_length=10, max_length=150, required=False, widget=TextInput())
    phone = CharField(min_length=10, max_length=12, required=True, widget=TextInput())
    email = CharField(min_length=5, max_length=50, required=False, widget=TextInput())
    birthday = DateField(required=False, widget=SelectDateWidget(years=range(current_year, 1899, -1)))
    class Meta:
        model = Contact
        fields = ['name', 'address', 'phone', 'email', 'birthday']