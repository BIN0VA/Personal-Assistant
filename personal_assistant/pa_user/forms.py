from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
    UserCreationForm,
)
from django.contrib.auth.models import User
from django.forms import (
    CharField,
    EmailField,
    EmailInput,
    PasswordInput,
    TextInput,
)

from pa_core.forms import FormHelper


USERNAME = {'min_length': 3, 'max_length': 16, 'required': True}


class PaUserAuthenticationForm(AuthenticationForm):
    username = CharField(
        widget=TextInput(FormHelper.attributes('username', 'me@example.com')),
        **USERNAME,
    )

    password = CharField(
        required=True,
        widget=PasswordInput(FormHelper.attributes('password', '****')),
    )

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super().__init__(*args, **kwargs)

        FormHelper.validate(self)

    class Meta:
        model = User
        fields = ('username', 'password')


class PaUserCreationForm(UserCreationForm):
    username = CharField(
        widget=TextInput(FormHelper.attributes('username', 'Nickname')),
        **USERNAME,
    )

    email = EmailField(
        min_length=7,
        max_length=40,
        required=True,
        widget=EmailInput(FormHelper.attributes('email', 'me@example.com')),
    )

    password1 = CharField(
        required=True,
        widget=PasswordInput(FormHelper.attributes('password', '****')),
    )

    password2 = CharField(
        required=True,
        widget=PasswordInput(FormHelper.attributes('repeat-password', '****')),
    )

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super().__init__(*args, **kwargs)

        FormHelper.validate(self)

    def save(self, commit: bool = True):
        user = super().save(commit=False)

        user.is_active = False

        if commit:
            user.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class PaUserPasswordResetForm(PasswordResetForm):
    email = EmailField(
        max_length=254,
        widget=EmailInput(FormHelper.attributes('email', 'me@example.com')),
    )

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super().__init__(*args, **kwargs)

        FormHelper.validate(self)


class PaUserSetPasswordForm(SetPasswordForm):
    new_password1 = CharField(
        required=True,
        strip=False,
        widget=PasswordInput(FormHelper.attributes('password', '****')),
    )

    new_password2 = CharField(
        required=True,
        strip=False,
        widget=PasswordInput(FormHelper.attributes('repeat-password', '****')),
    )

    def __init__(self, user, *args: tuple, **kwargs: dict) -> None:
        super().__init__(user, *args, **kwargs)

        FormHelper.validate(self)
