from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import NoReverseMatch, reverse


@login_required
def home(request: WSGIRequest) -> HttpResponse:
    return render(request, 'pa_core/home.html')


def overview(
    request: WSGIRequest,
    entity: str,
    items: list,
    context: dict = {},
    title: str = None
) -> HttpResponse:
    try:
        url = reverse(f'pa_{entity}:create')
    except NoReverseMatch:
        url = None

    return render(
        request,
        f'pa_{entity}/overview.html',
        {
            'title': title or f'{entity.title()}s',
            'url': url,
            'items': items,
            **context,
        },
    )
