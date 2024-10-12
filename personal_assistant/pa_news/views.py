from bs4 import BeautifulSoup
from django.shortcuts import render
from requests import get


def recent(request):
    url = 'https://ua.korrespondent.net/'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    news_block = soup.find('div', class_='time-articles')

    if news_block:
        articles = news_block.find_all('div', class_='article')

        for article in articles:
            time = article.find('div', class_='article__time').text.strip()
            title_tag = article.find('div', class_='article__title').find('a')
            title = title_tag.text.strip()
            link = title_tag['href']

            headlines.append({
                'title': title,
                'link': link,
                'time': time
            })

    return render(request, 'pa_news/recent.html', {'headlines': headlines})


def bank(request):
    items = []

    if (response := get('https://finance.i.ua/')).status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Знаходимо таблицю курсів валют
        rates_table = soup.find('tbody', class_='bank_rates_usd')

        # Ітеруємо через всі рядки в таблиці
        for row in rates_table.find_all('tr'):
            nodes = [
                row.find('th', class_='td-title'),
                row.find('td', class_='buy_rate').span,
                row.find('td', class_='sell_rate').span,
            ]

            items.append([node.text.strip() for node in nodes])

    return render(
        request,
        'pa_news/bank.html',
        {
            'title': 'Dollar exchange rate in different banks',
            'items': items,
        },
    )
