from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect

from accounts.forms import CustomUserCreationForm


class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('tasks:index')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    context = {'user': request.user}
    return render(request, 'accounts/profile.html', context)
