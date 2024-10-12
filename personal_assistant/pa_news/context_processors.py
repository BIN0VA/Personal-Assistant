from bs4 import BeautifulSoup
from django.core.handlers.wsgi import WSGIRequest
from requests import get


def global_context(request: WSGIRequest) -> dict:
    items = {}

    if (response := get('https://finance.i.ua/')).status_code != 200:
        return items

    soup = BeautifulSoup(response.text, 'html.parser')

    # Знаходимо таблицю з курсами
    if table := soup.find('table'):
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
                    type: cells[delta].find('span').find('span').text.strip()
                    for delta, type in enumerate(['Buy', 'Sell', 'NBU'])
                },
            }

    return {'currencies': items}
