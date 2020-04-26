from django.db import models

from accounts.models import CustomUser


class TaskStatus(models.Model):
    name = models.CharField(
        blank=False,
        max_length=255,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Task Statuses'


class Tag(models.Model):
    name = models.CharField(
        blank=False,
        unique=True,
        max_length=255,
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(
        blank=False,
        max_length=255,
    )
    description = models.TextField(
        blank=True
    )
    status = models.ForeignKey(
        TaskStatus,
        on_delete=models.PROTECT,
        blank=False,
    )
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=False,
        related_name='created_tasks',
    )
    assigned_to = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='assigned_tasks',
        blank=True
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
    )

    def __str__(self):
        return self.name
