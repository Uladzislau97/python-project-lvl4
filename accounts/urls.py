from django.urls import path, include

from accounts.views import RegistrationView, profile


app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', profile, name='profile')
]
