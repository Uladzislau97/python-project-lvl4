from django.views.generic.list import ListView

from tasks.models import (
    Task,
    TaskStatus,
    Tag,
)


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'


class TaskStatusListView(ListView):
    model = TaskStatus
    template_name = 'tasks/task_status_list.html'


class TagListView(ListView):
    model = Tag
    template_name = 'tasks/tag_list.html'
