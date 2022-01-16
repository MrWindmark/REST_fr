from django.db import models
from uuid import uuid4


# Create your models here.
class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4())
    name = models.CharField(max_length=64, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Notes(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4())
    title = models.CharField(max_length=32, blank=True, unique=False)
    inner_text = models.TextField(blank=True)
    task_date = models.DateField(verbose_name='Дата выполнения', name='Дата')
    is_complited = models.BooleanField(default=False)
    project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
