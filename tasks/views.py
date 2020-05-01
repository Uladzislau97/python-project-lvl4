from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from tasks.models import (
    Task,
    TaskStatus,
    Tag,
)
from tasks.filter import TaskFilter


class TaskListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Task
    template_name = 'tasks/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TaskFilter(self.request.GET)
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    login = '/login/'
    model = Task
    template_name = 'tasks/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_list'] = context['object'].tags.all()
        return context


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


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:task_list')


class TaskStatusListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = TaskStatus
    template_name = 'tasks/statuses/task_status_list.html'


class TaskStatusCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = TaskStatus
    fields = ['name']
    template_name = 'tasks/statuses/task_status_form.html'
    success_url = reverse_lazy('tasks:task_status_list')


class TaskStatusDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = TaskStatus
    template_name = 'tasks/statuses/task_status_confirm_delete.html'
    success_url = reverse_lazy('tasks:task_status_list')


class TagListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Tag
    template_name = 'tasks/tags/tag_list.html'


class TagCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Tag
    fields = ['name']
    template_name = 'tasks/tags/tag_form.html'
    success_url = reverse_lazy('tasks:tag_list')


class TagDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Tag
    template_name = 'tasks/tags/tag_confirm_delete.html'
    success_url = reverse_lazy('tasks:tag_list')
