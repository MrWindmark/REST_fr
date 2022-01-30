from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class Groups(models.Model):
    name = models.CharField(max_length=32, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=64, null=False, unique=True)
    email = models.EmailField(unique=True, max_length=254)
    category = models.CharField(max_length=2, null=False,
                                choices=(('UR', 'User'), ('AD', 'Admin'), ('MD', 'Modaretor')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
