from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from apps.core.base_models import ActiveSoftDeleteModel, TimeStampedModel
from apps.users.managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin, ActiveSoftDeleteModel, TimeStampedModel):
    class Gender(models.TextChoices):
        male = "male", "Male"
        female = "female", "Female"
        other = "other", "Other"

    email = models.EmailField(
        unique=True
    )

    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    birth_date = models.DateField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender,
        null=True,
        blank=True
    )

    is_tenant = models.BooleanField(default=True)
    is_landlord = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'em_users_users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
