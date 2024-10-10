
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import NoteForm
from .models import Note



def note(request):
    notes = Note.objects.all()
    return render(request, 'pa_note/note_list.html', {'notes': notes})


class NoteCreateView(View):
    def get(self, request):
        form = NoteForm()
        return render(request, 'pa_note/add_note.html', {'form': form})

    def post(self, request):
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pa_note:note')
        return render(request, 'pa_note/add_note.html', {'form': form})


class NoteDeleteView(View):
    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        return redirect('pa_note:note')


class NoteUpdateView(View):
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
