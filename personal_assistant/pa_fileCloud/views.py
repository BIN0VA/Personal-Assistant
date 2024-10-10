from django.shortcuts import render, redirect
from .forms import PaFileUploadForm
from .models import PaUploadedFile

def upload_file(request):
    if request.method == 'POST':
        form = PaFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = PaFileUploadForm()
    return render(request, 'upload.html', {'form': form})

def file_list(request):
    files = PaUploadedFile.objects.all()
    return render(request, 'file_list.html', {'files': files})

def filter_files_by_category(request, category):
    files = PaUploadedFile.objects.filter(category=category)
    return render(request, 'file_list.html', {'files': files})