from abc import ABC

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LoginView,
    PasswordResetConfirmView,
    PasswordResetView,
)
from django.contrib.messages import success
from django.contrib.messages.views import SuccessMessageMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.html import format_html

from pa_core.views import FormView, Response
from .forms import (
    PaUserAuthenticationForm,
    PaUserCreationForm,
    PaUserPasswordResetForm,
    PaUserSetPasswordForm,
)


class PaUserLoginView(LoginView):
    template_name = 'pa_user/login.html'
    form_class = PaUserAuthenticationForm
    redirect_authenticated_user = True


class PaUserCreationView(FormView):
    template_name = 'pa_user/register/form.html'
    form_class = PaUserCreationForm

    def _guest(self) -> bool:
        return False

    def post(self, request: WSGIRequest) -> Response:
        success(
            request,
            'A welcome message with further instructions has been sent to '
            'your email address.',
        )

        return super().post(request)


class PaUserPasswordResetViewBase(ABC, SuccessMessageMixin):
    success_url = reverse_lazy('pa_core:home')


class PaUserPasswordResetView(PaUserPasswordResetViewBase, PasswordResetView):
    form_class = PaUserPasswordResetForm
    template_name = 'pa_user/reset/begin.html'
    email_template_name = 'pa_user/reset/email.html'
    html_email_template_name = 'pa_user/reset/email.html'
    subject_template_name = 'pa_user/reset/subject.txt'

    def get_success_message(self, cleaned_data):
        return format_html(
            'An email with instructions to reset your password has been sent '
            'to <b>{}</b>.',
            cleaned_data['email'],
        )


class PaUserPasswordResetConfirmView(
    PaUserPasswordResetViewBase,
    PasswordResetConfirmView
):
    form_class = PaUserSetPasswordForm
    template_name = 'pa_user/reset/confirm.html'
    success_message = 'Password reset complete!'


@login_required
def signout(request: WSGIRequest) -> HttpResponsePermanentRedirect:
    logout(request)

    return redirect('pa_core:home')
