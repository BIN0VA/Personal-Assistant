from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.forms import CharField, EmailField, EmailInput, PasswordInput, \
    TextInput

from pa_core.forms import FormHelper


class PaUserAuthenticationForm(AuthenticationForm):
    username = CharField(
        max_length=16,
        min_length=3,
        required=True,
        widget=TextInput(FormHelper.attributes('username', 'me@example.com')),
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


class PaUserPasswordResetForm(PasswordResetForm):
    email = EmailField(
        max_length=254,
        widget=EmailInput(FormHelper.attributes('email', 'me@example.com')),
    )

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super().__init__(*args, **kwargs)

        FormHelper.validate(self)
