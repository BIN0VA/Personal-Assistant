from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .context_processors import global_context


@login_required
def home(request: WSGIRequest) -> HttpResponse:
    return render(request, 'pa_core/home.html')


@login_required
def search(request: WSGIRequest) -> HttpResponsePermanentRedirect:
    entity_types = global_context(request)['search']
    first_entity_type = list(entity_types.keys())[0]
    active_entity_type = first_entity_type

    for current_entity_type, active in entity_types.items():
        if active:
            active_entity_type = current_entity_type

            break

    if active_entity_type != first_entity_type:
        active_entity_type = active_entity_type[:-1]

    url = reverse(f'pa_{active_entity_type}:home')

    return redirect(f'{url}?{urlencode(request.GET)}')


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
