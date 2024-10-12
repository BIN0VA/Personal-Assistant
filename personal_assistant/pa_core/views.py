from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from pa_news.views import scrape_currency


@login_required
def home(request: WSGIRequest) -> HttpResponse:
    items = {}

    for item in scrape_currency()['rates']:
        match item['currency']:
            case 'USD': icon = 'dollar'
            case 'EUR': icon = 'euro'
            case _: icon = 'exchange'

        items[item['currency']] = {
            'icon': icon,
            'rates': list(item.values())[1:],
        }

    return render(request, 'pa_core/home.html', {'currencies': items})


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
