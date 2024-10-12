from django.core.handlers.wsgi import WSGIRequest

from .views import scrape_currency


def global_context(request: WSGIRequest) -> dict:
    return {'currencies': scrape_currency()}
