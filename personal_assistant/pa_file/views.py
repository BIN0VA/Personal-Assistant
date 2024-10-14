from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from pa_core.views import overview, Response
from .forms import PaFileUploadForm
from .models import File


@login_required
def upload(request: WSGIRequest) -> Response:
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
def main(request: WSGIRequest, category: str = None) -> HttpResponse:
    categories = {key: value for key, value in File.CATEGORIES}
    filters = {'user': request.user}

    if category:
        for key, value in File.CATEGORIES:
            if value.lower() == category:
                filters['category'] = key
                break

    files = File.objects.filter(**filters)

    return overview(
        request,
        'file',
        {file.file.url: categories[file.category] for file in files},
        {'types': categories.values()},
        icon='file-earmark-fill',
    )
