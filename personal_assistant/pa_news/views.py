from bs4 import BeautifulSoup
from requests import get

from pa_core.views import overview


def scrape(url: str) -> BeautifulSoup | None:
    return BeautifulSoup(response.text, 'lxml') \
        if (response := get(url)).status_code == 200 else None


def bank(request):
    items = []

    if soup := scrape('https://finance.i.ua/'):
        # Ітеруємо через всі рядки в таблиці
        for row in soup.find('tbody', class_='bank_rates_usd').find_all('tr'):
            nodes = [
                row.find('th', class_='td-title'),
                row.find('td', class_='buy_rate').span,
                row.find('td', class_='sell_rate').span,
            ]

            items.append([node.text.strip() for node in nodes])

    return overview(
        request,
        'news',
        items,
        title='Dollar exchange rate in different banks',
    )
