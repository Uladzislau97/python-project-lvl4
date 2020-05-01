from django.urls import path, include
from django.contrib.auth.views import PasswordChangeDoneView

from accounts.views import (
    RegistrationView,
    ProfileView,
    CustomPasswordChangeView,
)


app_name = 'accounts'
urlpatterns = [
    path(
        'password_change/',
        CustomPasswordChangeView.as_view(),
        name='password_change'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='registration/password_change_done.html'
        ),
        name='password_change_done'
    ),
    path('', include('django.contrib.auth.urls')),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
]
