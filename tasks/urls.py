from django.urls import path

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
        TaskListView.as_view(),
        name='task_list',
    ),
    path(
        'add/',
        TaskCreateView.as_view(),
        name='task_add',
    ),
    path(
        '<int:pk>/edit',
        TaskUpdateView.as_view(),
        name='taks_edit',
    ),
    path(
        'statuses/',
        TaskStatusListView.as_view(),
        name='task_status_list',
    ),
    path(
        'tags/',
        TagListView.as_view(),
        name='tag_list',
    ),
]
