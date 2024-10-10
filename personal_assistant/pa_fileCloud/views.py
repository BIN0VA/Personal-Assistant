from django.shortcuts import render, redirect
from .forms import PaFileUploadForm
from .models import PaUploadedFile
from django.contrib.auth.decorators import login_required

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = PaFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user  # Прив'язка файлу до поточного користувача
            uploaded_file.save()
            return redirect('file_list')
    else:
        form = PaFileUploadForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def file_list(request):
    files = PaUploadedFile.objects.filter(user=request.user)  # Показуємо тільки файли поточного користувача
    return render(request, 'file_list.html', {'files': files})

@login_required
def filter_files_by_category(request, category):
    files = PaUploadedFile.objects.filter(user=request.user, category=category)  # Фільтрація тільки файлів користувача
    return render(request, 'file_list.html', {'files': files})
