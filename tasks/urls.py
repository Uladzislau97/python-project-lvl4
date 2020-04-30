from django.urls import path
from django.contrib.auth.decorators import login_required

from tasks.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskStatusListView,
    TagListView,
)

app_name = 'tasks'
urlpatterns = [
    path(
        '',
        login_required(TaskListView.as_view()),
        name='task_list',
    ),
    path(
        'add/',
        login_required(TaskCreateView.as_view()),
        name='task_add',
    ),
    path(
        '<int:pk>/edit',
        login_required(TaskUpdateView.as_view()),
        name='taks_edit',
    ),
    path(
        'statuses/',
        login_required(TaskStatusListView.as_view()),
        name='task_status_list',
    ),
    path(
        'tags/',
        login_required(TagListView.as_view()),
        name='tag_list',
    ),
]
