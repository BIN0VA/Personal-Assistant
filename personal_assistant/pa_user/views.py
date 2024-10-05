from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import redirect


@login_required
def signout(request: WSGIRequest) -> HttpResponsePermanentRedirect:
    logout(request)

    return redirect('pa_core:home')
