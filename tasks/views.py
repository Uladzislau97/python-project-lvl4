from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from tasks.models import (
    Task,
    TaskStatus,
    Tag,
)


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'


class TaskCreateView(CreateView):
    model = Task
    fields = [
        'name',
        'description',
        'status',
        'creator',
        'assigned_to',
        'tags',
    ]
    success_url = reverse_lazy('tasks:task_list')


class TaskStatusListView(ListView):
    model = TaskStatus
    template_name = 'tasks/task_status_list.html'


class TagListView(ListView):
    model = Tag
    template_name = 'tasks/tag_list.html'
