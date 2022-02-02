import datetime

from django.db import models
from uuid import uuid4
from userapp.models import User


# Create your models here.
class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, unique=True, null=False)
    name = models.CharField(max_length=64, blank=False)
    repo_link = models.CharField(max_length=256, blank=True)
    included_users = models.ManyToManyField(User)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Notes(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, unique=True, null=False)
    title = models.CharField(max_length=48, blank=True, unique=False)
    inner_text = models.TextField(blank=True)
    task_date = models.DateField(verbose_name='Completion date', name='Date', default=datetime.date.today())
    is_complited = models.BooleanField(default=False)
    project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, null=False)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
