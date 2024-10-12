from django.shortcuts import render, redirect
from .models import Tag
from .forms import TagForm

def main(request):
    tags =  Tag.objects.all()
    context = {"tags":tags}

    return render(request, 'tags/tags.html', context)

def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='pa_tags:main')
        else:
            return render(request, 'tags/add_tag.html', {'form': form})

    return render(request, 'tags/add_tag.html', {'form': TagForm()})

def delete(request, tag_id):
    Tag.objects.get(pk=tag_id).delete()
    return redirect(to='pa_tags:main')
