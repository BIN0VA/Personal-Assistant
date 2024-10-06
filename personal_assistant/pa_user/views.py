from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LoginView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import (
    PaUserAuthenticationForm,
    PaUserPasswordResetForm,
    PaUserSetPasswordForm
)


class PaUserLoginView(LoginView):
    template_name = 'pa_user/login.html'
    form_class = PaUserAuthenticationForm
    redirect_authenticated_user = True


class PaUserPasswordResetView(PasswordResetView, SuccessMessageMixin):
    form_class = PaUserPasswordResetForm
    template_name = 'pa_user/reset/begin.html'
    email_template_name = 'pa_user/reset/email.html'
    html_email_template_name = 'pa_user/reset/email.html'
    success_url = reverse_lazy('pa_user:done')
    success_message = ('An email with instructions to reset your password has '
                       'been sent to %(email)s.')
    subject_template_name = 'pa_user/reset/subject.txt'


class PaUserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'pa_user/reset/done.html'


class PaUserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = PaUserSetPasswordForm
    template_name = 'pa_user/reset/confirm.html'
    success_url = reverse_lazy('pa_user:complete')


class PaUserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'pa_user/reset/complete.html'


@login_required
def signout(request: WSGIRequest) -> HttpResponsePermanentRedirect:
    logout(request)

    return redirect('pa_core:home')
