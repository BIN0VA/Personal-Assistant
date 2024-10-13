from django.core.handlers.wsgi import WSGIRequest
from django.template.loader import render_to_string

from .models import News, Rate


def news_section(request: WSGIRequest):
    items = News.objects.all()

    return render_to_string('pa_news/recent.html', {'items': items}) \
        if items else ''


def exchange_rates_section(request: WSGIRequest):
    items = {}

    for rate in Rate.objects.filter(bank=False):
        match rate.name:
            case 'USD': icon = 'dollar'
            case 'EUR': icon = 'euro'
            case _: icon = None

        items[rate.name] = {
            'icon': icon,
            'rates': {
                'Buy': rate.buy,
                'Sell': rate.sell,
            },
        }

    return render_to_string(
        'pa_news/currency.html',
        {
            'items': items,
            'path': request.path,
        },
    ) if items else ''


def global_context(request: WSGIRequest) -> dict:
    return {
        name.removesuffix('_section'): callback(request)
        for name, callback in globals().items() if name.endswith('_section')
    }
