from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.contrib.messages import warning
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Count
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from pa_core.views import overview
from pa_note.models import Note
from .models import Tag
from .forms import TagForm


@login_required
def main(request: WSGIRequest):
    if request.method == 'POST':
        if (form := TagForm(request.POST)).is_valid():
            tag = form.save(False)
            tag.user = request.user
            tag.save()

            return redirect('pa_tag:home')
    else:
        GET = request.GET

        if GET.get('type', 'contacts').lower() == 'tags' and GET.get('query'):
            return redirect(f'{reverse('pa_note:home')}?{urlencode(GET)}')

        form = TagForm()

    items = {
        tag.name: tag.id if (
            not tag.usages and
            (request.user.is_superuser or tag.user == request.user)
        ) else 0
        for tag in Tag.objects.annotate(usages=Count('notes'))
    }

    return overview(request, 'tag', items, {'form': form}, 'tag-fill')


@login_required
def delete(request: WSGIRequest, tag_id: int) -> HttpResponsePermanentRedirect:
    filters = {}

    if not request.user.is_superuser:
        filters['user'] = request.user

    tag = get_object_or_404(Tag, id=tag_id, **filters)

    if Note.objects.filter(tags=tag):
        warning(
            request,
            f'The {tag} tag is used in some notes so it can not be deleted.',
        )
    else:
        tag.delete()

    return redirect('pa_tag:home')
