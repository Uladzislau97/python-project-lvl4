from django.urls import path

from tasks.views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskStatusListView,
    TaskStatusCreateView,
    TaskStatusDeleteView,
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
        '<int:pk>',
        TaskDetailView.as_view(),
        name='task_detail',
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
        'statuses/add',
        TaskStatusCreateView.as_view(),
        name='task_status_add',
    ),
    path(
        'statuses/<int:pk>/delete',
        TaskStatusDeleteView.as_view(),
        name='task_status_delete',
    ),
    path(
        'tags/',
        TagListView.as_view(),
        name='tag_list',
    ),
]
