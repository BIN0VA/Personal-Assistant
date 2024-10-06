import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def scrape_general_news():
    url = 'https://ua.korrespondent.net/'
    response = requests.get(url)
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

def display_news(request):
    context = {}

    if request.method == 'POST':
        category = request.POST.get('category')

        if category == 'general_news':
            context['headlines'] = scrape_general_news()
        elif category == 'weather':
            context['headlines'] = [{'title': 'Погода: Заглушка', 'time': '', 'link': '#'}]  # Заглушка для погоди
        elif category == 'currency':
            context['headlines'] = [{'title': 'Курс валют: Заглушка', 'time': '', 'link': '#'}]  # Заглушка для курсу валют

    return render(request, 'pa_news/news_summary.html', context)