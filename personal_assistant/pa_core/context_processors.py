from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse


def global_context(request: WSGIRequest) -> dict:
    teammates = {
        'B': 'derso001',
        'I': 'DeTr1ll',
        'N': 'sholohova27',
        'O': 'lexhouk',
        'V': 'mzLeVit',
        'A': 'alina-kylymnyk',
    }

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
        'project_name': settings.PROJECT_NAME,
        'project_team': ''.join([
            f'<a href="https://github.com/{nickname}" target="_blank">{letter}'
            '</a>'
            for letter, nickname in teammates.items()
        ]),
        'search': {
            current_entity_type: current_entity_type == active_entity_type
            for current_entity_type in entity_types
        },
    }
