from django.db import models
from apps.core.models import AbstractBaseModel


class APIKey(AbstractBaseModel):
    app_name = models.CharField(max_length=50, unique=True)
    key = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.app_name

    class Meta:
        verbose_name_plural = 'API Keys'
