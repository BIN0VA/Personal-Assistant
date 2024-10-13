from django.shortcuts import render, redirect, get_object_or_404

from .models import Tag
from .forms import TagForm


def tags(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pa_tag:tags')
    else:
        form = TagForm()

    items = Tag.objects.all()
    return render(request, 'pa_tags/list.html', {'items': items, 'form': form})

def delete(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    tag.delete()
    return redirect('pa_tag:tags')
