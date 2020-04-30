from django.views.generic.list import ListView

from tasks.models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
