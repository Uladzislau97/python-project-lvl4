from django.urls import path

from tasks.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
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
        name='task_edit',
    ),
    path(
        '<int:pk>/delete',
        TaskDeleteView.as_view(),
        name='task_delete',
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
