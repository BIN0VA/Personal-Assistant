from django.contrib.postgres.search import SearchVector
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View

from pa_core.views import overview
from pa_tag.models import Tag
from .forms import NoteForm
from .models import Note


@login_required
def note(request):
    items = Note.objects.filter(user=request.user)

    if query := request.GET.get('query'):
        match request.GET.get('type', 'contacts').lower():
            case 'notes':
                if connection.vendor == 'postgresql':
                    items = items.annotate(search=SearchVector('name')) \
                        .filter(search=query)
                else:
                    items = items.filter(name__icontains=query)

            case 'tags':
                items = items.filter(tags__name__icontains=query)
    else:
        items = items.all()

    return overview(request, 'note', items, icon='sticky')


@method_decorator(login_required, name='dispatch')
class CreateView(View):
    def get(self, request):
        return render(
            request,
            'pa_note/add_note.html',
            {
                'form': NoteForm(),
                'tags': Tag.objects.all(),
            },
        )

    def post(self, request):
        tags = Tag.objects

        if (form := NoteForm(request.POST)).is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()

            ids = request.POST.getlist('tags')

            for tag in tags.filter(id__in=ids).iterator():
                note.tags.add(tag)

            return redirect('pa_note:home')

        return render(
            request,
            'pa_note/add_note.html',
            {
                'form': form,
                'tags': tags.all(),
            },
        )


@method_decorator(login_required, name='dispatch')
class DeleteView(View):
    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        note.delete()
        return redirect('pa_note:home')


@method_decorator(login_required, name='dispatch')
class UpdateView(View):
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        form = NoteForm(instance=note)
        return render(
            request,
            'pa_note/edit_note.html',
            {'form': form, 'note': note},
        )

    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('pa_note:home')
        return render(
            request,
            'pa_note/edit_note.html',
            {'form': form, 'note': note},
        )


@method_decorator(login_required, name='dispatch')
class DoneUpdateView(View):
    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        note.done = True
        note.save()
        return redirect('pa_note:home')
