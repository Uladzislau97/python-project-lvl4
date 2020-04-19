from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from accounts.forms import CustomUserCreationForm


class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('tasks:index')
