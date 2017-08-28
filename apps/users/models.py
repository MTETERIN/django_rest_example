from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.core.models import AbstractBaseModel


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            is_active=is_active,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser, AbstractBaseModel):
    """User class definition.

        Attributes:
            username     The nickname or login of the user.
            email  Email address of the user.
            email_confirmation_token  Token for email confirmation.
            reset_key  Token for changing password.
            role  Role of the user.
    """
    ROLE_CHOICES = (
        ('none', 'Without role'),
    )

    username = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    email = models.EmailField(unique=True)
    email_confirmation_token = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    reset_key = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    role = models.CharField(
        choices=ROLE_CHOICES,
        max_length=32,
        default='none',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        """
        User object's string representation.
        """
        return self.email

    class Meta:
        verbose_name_plural = 'Users'
