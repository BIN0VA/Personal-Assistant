from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.contrib.messages import info
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.views import View
from requests import get

from pa_core.views import overview
from .models import News, Rate


def scrape(url: str) -> BeautifulSoup | None:
    return BeautifulSoup(response.text, 'lxml') \
        if (response := get(url)).status_code == 200 else None


@login_required
def bank(request):
    return overview(
        request,
        'news',
        Rate.objects.filter(bank=True),
        title='Dollar exchange rate in different banks',
    )


Response = HttpResponse | HttpResponsePermanentRedirect


class UpdateView(View):
    def dispatch(self, request: WSGIRequest) -> Response:
        return super().dispatch(request) if request.user.is_superuser \
            else redirect('pa_core:home')

    def get(self, request: WSGIRequest) -> HttpResponse:
        info(
            request,
            '''Press the button below to see the first news and data on
            exchange rates, whether those displayed at the moment have been
            updated. After the first successful launch, information on currency
            rates should appear on all pages (it will be displayed immediately
            after the navigation section). Also, a news feed should appear at
            the bottom of the main page.''',
        )

        return render(request, 'pa_news/update.html')

    def post(self, request: WSGIRequest) -> HttpResponsePermanentRedirect:
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

        if items:
            News.objects.all().delete()

            for item in items:
                News.objects.create(**item)

        items = []

        if (
            (soup := scrape('https://finance.i.ua/')) and
            (table := soup.find('table'))
        ):
            for row in table.find('tbody').find_all('tr'):
                cells = row.find_all('td')

                items.append({
                    'name': row.find('th').text.strip(),
                    **{
                        type: cells[delta].find('span').find('span').text.
                        strip()
                        for delta, type in enumerate(['buy', 'sell'])
                    },
                })

        if cleaned := len(items) > 0:
            Rate.objects.all().delete()

            for item in items:
                Rate.objects.create(**item)

        items = []

        if soup := scrape('https://finance.i.ua/'):
            wrapper = soup.find('tbody', class_='bank_rates_usd')

            for row in wrapper.find_all('tr'):
                nodes = {
                    'name': row.find('th', class_='td-title'),
                    'buy': row.find('td', class_='buy_rate').span,
                    'sell': row.find('td', class_='sell_rate').span,
                }

                items.append({
                    name: node.text.strip() for name, node in nodes.items()
                })

        if items:
            if not cleaned:
                Rate.objects.all().delete()

            for item in items:
                Rate.objects.create(**item, bank=True)

        return redirect('pa_core:home')
