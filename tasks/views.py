from django.shortcuts import render, redirect


def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    context = {'user': request.user}
    return render(request, 'tasks/index.html', context)
