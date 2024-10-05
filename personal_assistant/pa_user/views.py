from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import PaUserPasswordResetForm


class PaUserPasswordResetView(PasswordResetView, SuccessMessageMixin):
    form_class = PaUserPasswordResetForm
    template_name = 'pa_user/reset.html'
    email_template_name = 'pa_user/reset_email.html'
    success_url = reverse_lazy('pa_user:login')
    success_message = ('An email with instructions to reset your password has '
                       'been sent to %(email)s.')


@login_required
def signout(request: WSGIRequest) -> HttpResponsePermanentRedirect:
    logout(request)

    return redirect('pa_core:home')
