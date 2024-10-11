
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db import connection
from django.contrib.postgres.search import SearchVector


from .forms import NoteForm, NoteDoneForm
from .models import Note

def note(request):
    notes = Note.objects.all()
    return render(request, 'pa_note/note_list.html', {'notes': notes})


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
        return render(request, 'pa_note/edit_note.html', {'form': form, 'note': note})


    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('pa_note:note')
        return render(request, 'pa_note/edit_note.html', {'form': form, 'note': note})


class DoneUpdateView(View):
    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        note.done = True
        note.save()
        return redirect('pa_note:note')


def universal_notes_search(query):
    if connection.vendor =='postgresql':
        return Note.objects.annotate(search=SearchVector('name', 'description')).filter(search=query)
    else:
        return Note.objects.filter(name__icontains=query) | Note.objects.filter(description__icontains=query)


def notes_search(request):
    query = request.GET.get('q')
    if query:
        result = universal_notes_search(query)
    else:
        result = Note.objects.all()
    return render(request, 'pa_note/note_list.html', {'notes': result})