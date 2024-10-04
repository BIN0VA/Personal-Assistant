from django.contrib.auth.views import LoginView
from django.urls import path

from .forms import LoginForm
from .views import signout

app_name = 'pa_user'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name='pa_user/login.html',
            form_class=LoginForm,
            redirect_authenticated_user=True,
        ),
        name='login',
    ),
    path('logout/', signout, name='logout'),
]
