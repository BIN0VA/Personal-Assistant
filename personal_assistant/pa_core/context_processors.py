from django.apps import apps
from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse


def project_name_section(request: WSGIRequest) -> str:
    return settings.PROJECT_NAME


def project_team_section(request: WSGIRequest) -> str:
    teammates = {
        'B': 'derso001',
        'I': 'DeTr1ll',
        'N': 'sholohova27',
        'O': 'lexhouk',
        'V': 'mzLeVit',
        'A': 'alina-kylymnyk',
    }

    return ''.join([
        f'<a href="https://github.com/{nickname}" target="_blank">{letter}</a>'
        for letter, nickname in teammates.items()
    ])


def menu(request: WSGIRequest, class_: str, condition: bool = False) -> dict:
    items = {}

    for name in settings.PROJECT_APPS:
        app_config = apps.get_app_config(name)

        if (
            not hasattr(app_config, 'not_in_main_menu') and
            (not condition or not hasattr(app_config, 'not_in_user_menu'))
        ):
            url = reverse(f'{name}:home')
            classes = class_

            if request.path == url:
                classes += ' active'

            items[url] = {
                'label': app_config.verbose_name,
                'classes': classes,
            }

    return items


def main_menu_section(request: WSGIRequest) -> dict:
    return menu(request, 'nav-link')


def user_menu_section(request: WSGIRequest) -> dict:
    return menu(request, 'dropdown-item', True)


def search_section(request: WSGIRequest) -> str:
    entity_types = ('contacts', 'notes', 'tags')

    if request.GET.get('query'):
        active_entity_type = request.GET.get('type', entity_types[0]).lower()
    else:
        active_entity_type = entity_types[0]

        for delta, current_entity_type in enumerate(entity_types):
            suffix = current_entity_type[:-1] if delta else current_entity_type

            if request.path == reverse(f'pa_{suffix}:home'):
                active_entity_type = current_entity_type
                break

    if active_entity_type not in entity_types:
        active_entity_type = entity_types[0]

    return {
        current_entity_type: current_entity_type == active_entity_type
        for current_entity_type in entity_types
    }


def global_context(request: WSGIRequest) -> dict:
    return {
        name.removesuffix('_section'): callback(request)
        for name, callback in globals().items() if name.endswith('_section')
    }
