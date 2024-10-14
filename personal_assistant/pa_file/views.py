from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

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
    filters = {'user': request.user}

    if category:
        for key, value in File.CATEGORIES:
            if value.lower() == category:
                filters['category'] = key
                break

    files = File.objects.filter(**filters)

    if not category:
        files = files.order_by('category')

    tabs = {
        reverse('pa_file:home'): 'All Files',
        **{
            reverse('pa_file:category', args=[category[1].lower()]):
            category[1]
            for category in File.CATEGORIES
        },
    }

    tabs = {
        link:
        {
            'label': label,
            'classes': 'nav-link' +
            (' active' if request.path == link else ''),
        }
        for link, label in tabs.items()
    }

    return overview(request, 'file', files, {'tabs': tabs}, 'file-earmark')
