from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from tasks.models import (
    Task,
    TaskStatus,
    Tag,
)


class TaskListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Task
    template_name = 'tasks/task_list.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Task
    fields = [
        'name',
        'description',
        'status',
        'creator',
        'assigned_to',
        'tags',
    ]
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task_list')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Task
    fields = [
        'name',
        'description',
        'status',
        'creator',
        'assigned_to',
        'tags',
    ]
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task_list')


class TaskStatusListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = TaskStatus
    template_name = 'tasks/task_status_list.html'


class TagListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Tag
    template_name = 'tasks/tag_list.html'
