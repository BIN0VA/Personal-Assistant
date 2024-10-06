from django.urls import path

from .views import (
    PaUserLoginView,
    PaUserPasswordResetCompleteView as ResetCompleteView,
    PaUserPasswordResetConfirmView as Confirm,
    PaUserPasswordResetDoneView as PaUserDoneView,
    PaUserPasswordResetView,
    signout
)

app_name = 'pa_user'
url = 'reset-password/'

urlpatterns = [
    path('login/', PaUserLoginView.as_view(), name='login'),
    path('logout/', signout, name='logout'),
    path(url, PaUserPasswordResetView.as_view(), name='reset'),
    path(f'{url}done/', PaUserDoneView.as_view(), name='done'),
    path(f'{url}confirm/<uidb64>/<token>/', Confirm.as_view(), name='confirm'),
    path(f'{url}complete/', ResetCompleteView.as_view(), name='complete'),
]
