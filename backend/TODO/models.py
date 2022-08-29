from django.db import models
from django_filters import filters

from users.models import CustomUser
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    link_to_repo = models.URLField(max_length=120, null=True)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.title


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    CreatorUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Дата последнего изменения')

    date_from = filters.DateFilter(field_name='created_at', lookup_expr='date_gte')
    date_to = filters.DateFilter(field_name='created_at', lookup_expr='date_lte')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']

