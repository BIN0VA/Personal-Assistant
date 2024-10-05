from django.contrib.auth.views import LoginView, PasswordResetConfirmView
from django.urls import path

from .forms import PaUserAuthenticationForm
from .views import PaUserPasswordResetView, signout

app_name = 'pa_user'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name='pa_user/login.html',
            form_class=PaUserAuthenticationForm,
            redirect_authenticated_user=True,
        ),
        name='login',
    ),
    path('logout/', signout, name='logout'),
    path('reset-password/', PaUserPasswordResetView.as_view(), name='reset'),
    path(
        'reset-password/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(),
        name='reset_confirm',
    ),
]
