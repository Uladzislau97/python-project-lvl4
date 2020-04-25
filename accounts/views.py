from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView

from accounts.forms import CustomUserCreationForm


class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('tasks:index')


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('accounts:password_change_done')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    context = {'user': request.user}
    return render(request, 'accounts/profile.html', context)
