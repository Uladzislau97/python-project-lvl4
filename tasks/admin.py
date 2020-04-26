from django.contrib import admin

from tasks.models import (
    TaskStatus,
    Tag,
    Task,
)


admin.site.register(TaskStatus)
admin.site.register(Tag)
admin.site.register(Task)
