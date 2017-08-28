from django.db import models
from apps.core.models import AbstractBaseModel


class APIKey(AbstractBaseModel):
    """
    API key for different app access.
    """
    app_name = models.CharField(max_length=50, unique=True)
    key = models.CharField(max_length=40, unique=True)

    def __str__(self):
        """
        APIKey object's string representation.
        """
        return self.app_name

    class Meta:
        verbose_name_plural = 'API Keys'
