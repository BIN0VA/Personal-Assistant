from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from pa_core.views import overview
from .forms import NoteForm
from .models import Note


def note(request):
    return overview(request, 'note', Note.objects.all())


class CreateView(View):
    def get(self, request):
        form = NoteForm()
        return render(request, 'pa_note/add_note.html', {'form': form})

    def post(self, request):
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pa_note:note')
        return render(request, 'pa_note/add_note.html', {'form': form})


class DeleteView(View):
    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        return redirect('pa_note:note')


class UpdateView(View):
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        form = NoteForm(instance=note)
        return render(
            request,
            'pa_note/edit_note.html',
            {'form': form, 'note': note},
        )

    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('pa_note:note')
        return render(
            request,
            'pa_note/edit_note.html',
            {'form': form, 'note': note},
        )


class DoneUpdateView(View):
    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        note.done = True
        note.save()
        return redirect('pa_note:note')
