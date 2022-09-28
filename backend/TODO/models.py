from django.db import models
from django_filters import filters

from users.models import CustomUser
from django.utils import timezone

class Project(models.Model):
    CreatorUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, unique=True)
    link_to_repo = models.URLField(max_length=120, null=True)


    def __str__(self) -> str:
        return f'{self.CreatorUser} {self.title}'

    def delete(self, *args) -> None:
        return super().delete(*args)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    CreatorUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False, verbose_name="Completed")

    def __str__(self) -> str:
        return f'{self.CreatorUser} {self.project} {self.title}'

    def delete(self, *args) -> None:
        return super().delete(*args)

    class Meta:
        verbose_name = 'ToDo note'
        verbose_name_plural = 'ToDo notes'

