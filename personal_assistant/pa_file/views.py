from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from pa_core.views import overview
from .forms import PaFileUploadForm
from .models import File


@login_required
def upload(request):
    if request.method == 'POST':
        form = PaFileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = form.save(False)

            # Прив'язка файлу до поточного користувача
            uploaded_file.user = request.user

            uploaded_file.save()

            return redirect('pa_file:home')
    else:
        form = PaFileUploadForm()

    return render(request, 'pa_file/upload.html', {'form': form})


@login_required
def main(request):
    # Показуємо тільки файли поточного користувача
    files = File.objects.filter(user=request.user)

    return overview(request, 'file', files, icon='file-earmark-fill')


@login_required
def filter_files_by_category(request, category):
    # Фільтрація тільки файлів користувача
    files = File.objects.filter(user=request.user, category=category)

    return overview(request, 'file', files, icon='file-earmark-fill')
