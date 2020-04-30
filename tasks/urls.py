from django.urls import path
from django.contrib.auth.decorators import login_required

from tasks.views import TaskListView

app_name = 'tasks'
urlpatterns = [
    path(
        '',
        login_required(TaskListView.as_view()),
        name='task_list'
    ),
]
