from abc import ABC, abstractmethod
from typing import Any
from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponsePermanentRedirect, QueryDict
from django.shortcuts import redirect, render
from django.urls import NoReverseMatch, reverse
from django.views import View

from .context_processors import global_context


Response = HttpResponse | HttpResponsePermanentRedirect


class FormView(ABC, View):
    def _context(self) -> dict:
        return dict()

    @abstractmethod
    def _guest(self) -> bool:
        ...

    def _save(
        self,
        response: QueryDict,
        form: ModelForm,
        commit: bool = True
    ) -> Any:
        return form.save(commit)

    def dispatch(self, request: WSGIRequest) -> Response:
        if request.user.is_anonymous == self._guest():
            return redirect('pa_core:home')

        return super().dispatch(request)

    def get(self, request: WSGIRequest) -> HttpResponse:
        return render(
            request,
            self.template_name,
            {'form': self.form_class, **self._context()},
        )

    def post(self, request: WSGIRequest) -> Response:
        form = self.form_class(request.POST)

        if form.is_valid():
            self._save(request.POST, form)

            return redirect('pa_core:home')

        return render(
            request,
            self.template_name,
            {'form': form, **self._context()},
        )


@login_required
def home(request: WSGIRequest) -> HttpResponse:
    return render(request, 'pa_core/home.html')


@login_required
def search(request: WSGIRequest) -> HttpResponsePermanentRedirect:
    entity_types = global_context(request)['search']
    first_entity_type = list(entity_types.keys())[0]
    active_entity_type = first_entity_type

    for current_entity_type, active in entity_types.items():
        if active:
            active_entity_type = current_entity_type

            break

    if active_entity_type != first_entity_type:
        active_entity_type = active_entity_type[:-1]

    url = reverse(f'pa_{active_entity_type}:home')

    return redirect(f'{url}?{urlencode(request.GET)}')


def overview(
    request: WSGIRequest,
    entity: str,
    items: list,
    context: dict = {},
    title: str = None
) -> HttpResponse:
    try:
        url = reverse(f'pa_{entity}:create')
    except NoReverseMatch:
        url = None

    return render(
        request,
        f'pa_{entity}/overview.html',
        {
            'title': title or f'{entity.title()}s',
            'url': url,
            'items': items,
            **context,
        },
    )
