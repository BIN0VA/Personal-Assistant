from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


@login_required
def home(request: WSGIRequest) -> HttpResponse:
    return render(request, 'pa_core/home.html')


def overview(
    request: WSGIRequest,
    entity: str,
    items: str,
    context: dict = {},
    title: str = None
) -> HttpResponse:
    return render(
        request,
        f'pa_{entity}/overview.html',
        {
            'title': title or f'{entity.title()}s',
            'url': reverse(f'pa_{entity}:create'),
            'items': items,
            **context,
        },
    )
