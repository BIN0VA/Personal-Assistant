from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Tag
from .forms import TagForm


@login_required
def main(request):
    if request.method == 'POST':
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('pa_tag:home')
    else:
        GET = request.GET

        if GET.get('type', 'contacts').lower() == 'tags' and GET.get('type'):
            return redirect(f'{reverse('pa_note:home')}?{urlencode(GET)}')

        form = TagForm()

    items = Tag.objects.all()

    return render(request, 'pa_tag/list.html', {'items': items, 'form': form})


@login_required
def delete(request, tag_id):
    get_object_or_404(Tag, id=tag_id).delete()

    return redirect('pa_tag:home')
