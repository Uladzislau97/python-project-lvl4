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
    TagCreateView,
    TagDeleteView,
)

app_name = 'tasks'
urlpatterns = [
    path(
        '',
        TaskListView.as_view(),
        name='task_list',
    ),
    path(
        'new/',
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
        'statuses/new',
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
    path(
        'tags/new',
        TagCreateView.as_view(),
        name='tag_add',
    ),
    path(
        'tags/<int:pk>/delete',
        TagDeleteView.as_view(),
        name='tag_delete',
    ),
]
