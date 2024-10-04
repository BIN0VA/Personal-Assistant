from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import CharField, PasswordInput, TextInput

from pa_core.forms import FormHelper


USERNAME = {'min_length': 3, 'max_length': 16, 'required': True}


class LoginForm(AuthenticationForm):
    username = CharField(
        widget=TextInput(FormHelper.attributes('username', 'me@example.com')),
        **USERNAME,
    )

    password = CharField(
        required=True,
        widget=PasswordInput(FormHelper.attributes('password', 'Password')),
    )

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super().__init__(*args, **kwargs)

        FormHelper.validate(self)

    class Meta:
        model = User
        fields = ('username', 'password')
