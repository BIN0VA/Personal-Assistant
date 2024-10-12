from requests import get
from bs4 import BeautifulSoup
from django.shortcuts import render


def scrape_general_news():
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

    return headlines


def scrape_currency():
    url = "https://finance.i.ua/"
    response = get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Заголовок
        header = soup.find('h2').text.strip()

        # Список для зберігання курсів валют
        currency_rates = []

        # Знаходимо таблицю з курсами
        # Знаходимо таблицю (можливо, вам потрібно буде вказати точніший
        # селектор)
        table = soup.find('table')

        if table:
            # Збираємо всі рядки в таблиці
            rows = table.find('tbody').find_all('tr')

            for row in rows:
                # Збираємо дані з кожного рядка
                currency = row.find('th').text.strip()
                buy = row.find_all('td')[0].find('span').find('span').text.strip()  # Купівля
                sell = row.find_all('td')[1].find('span').find('span').text.strip()  # Продаж
                nbu = row.find_all('td')[2].find('span').find('span').text.strip()  # НБУ

                # Додаємо дані до списку
                currency_rates.append({
                    'currency': currency,
                    'buy': buy,
                    'sell': sell,
                    'nbu': nbu,
                })

        return {
            'header': header,
            'rates': currency_rates
        }
    else:
        return {
            'header': 'Не вдалося отримати курс валют',
            'rates': []
        }  # Обробка помилки


def scrape_currency_2():
    # Замініть на URL, з якого будете отримувати другий набір курсів
    url = "https://finance.i.ua/"
    response = get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    # Знаходимо заголовок
    title = soup.find('h2', text='Курс валют банків в Україні').text

    # Знаходимо таблицю курсів валют
    rates_table = soup.find('tbody', class_='bank_rates_usd')

    rates = []
    # Ітеруємо через всі рядки в таблиці
    for row in rates_table.find_all('tr'):
        bank_name = row.find('th', class_='td-title').text.strip()
        buy_rate = row.find('td', class_='buy_rate').span.text.strip()
        sell_rate = row.find('td', class_='sell_rate').span.text.strip()

        rates.append({
            'currency': bank_name,
            'buy': buy_rate,
            'sell': sell_rate,
        })

    return title, rates


def display_news(request):
    context = {}

    if request.method == 'POST':
        category = request.POST.get('category')

        if category == 'general_news':
            context['headlines'] = scrape_general_news()
        elif category == 'currency':
            currency_data = scrape_currency()
            context['header'] = currency_data['header']
            context['rates'] = currency_data['rates']
            # Викликаємо scrape_currency_2 і додаємо результати до контексту

            header_2, rates_2 = scrape_currency_2()
            context['header_2'] = header_2
            context['rates_2'] = rates_2

    return render(request, 'pa_news/news_summary.html', context)
