from django.urls import path, include

from accounts.views import RegistrationView


app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', RegistrationView.as_view(), name='registration'),
]
