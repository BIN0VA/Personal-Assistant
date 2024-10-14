from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from pa_core.views import overview
from .models import Tag
from .forms import TagForm


@login_required
def main(request):
    if request.method == 'POST':
        if (form := TagForm(request.POST)).is_valid():
            form.save()

            return redirect('pa_tag:home')
    else:
        GET = request.GET

        if GET.get('type', 'contacts').lower() == 'tags' and GET.get('query'):
            return redirect(f'{reverse('pa_note:home')}?{urlencode(GET)}')

        form = TagForm()

    items = Tag.objects.all()

    return overview(request, 'tag', items, {'form': form}, 'tag-fill')


@login_required
def delete(request, tag_id):
    get_object_or_404(Tag, id=tag_id).delete()

    return redirect('pa_tag:home')
