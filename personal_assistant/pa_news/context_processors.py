from django.core.handlers.wsgi import WSGIRequest
from django.template.loader import render_to_string

from .views import scrape


def news_section(request: WSGIRequest):
    items = []

    if (
        (soup := scrape('https://ua.korrespondent.net/')) and
        (news_block := soup.find('div', class_='time-articles'))
    ):
        for article in news_block.find_all('div', class_='article'):
            title = article.find('div', class_='article__title').find('a')

            items.append({
                'title': title.text.strip(),
                'link': title['href'],
                'time': article.find('div', class_='article__time').text.
                strip(),
            })

            if len(items) == 6:
                break

    return render_to_string('pa_news/recent.html', {'items': items}) \
        if items else ''


def exchange_rates_section(request: WSGIRequest):
    items = {}

    if (
        (soup := scrape('https://finance.i.ua/')) and
        (table := soup.find('table'))
    ):
        # Збираємо всі рядки в таблиці
        for row in table.find('tbody').find_all('tr'):
            # Збираємо дані з кожного рядка
            currency = row.find('th').text.strip()

            match currency:
                case 'USD': icon = 'dollar'
                case 'EUR': icon = 'euro'
                case _: icon = None

            cells = row.find_all('td')

            # Додаємо дані до словника
            items[currency] = {
                'icon': icon,
                'rates': {
                    type: cells[delta].find('span').find('span').text.
                    strip()
                    for delta, type in enumerate(['Buy', 'Sell', 'NBU'])
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
