from django.urls import path

from .views import (
    PaUserCreationView,
    PaUserLoginView,
    PaUserPasswordResetConfirmView as Confirm,
    PaUserPasswordResetView,
    signout,
)

app_name = 'pa_user'
url = 'reset-password/'

urlpatterns = [
    path('login/', PaUserLoginView.as_view(), name='login'),
    path('logout/', signout, name='logout'),
    path('register/', PaUserCreationView.as_view(), name='register'),
    path(url, PaUserPasswordResetView.as_view(), name='reset'),
    path(f'{url}confirm/<uidb64>/<token>/', Confirm.as_view(), name='confirm'),
]
