from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from users.managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
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
        choices=Gender.choices,
        null=True,
        blank=True
    )

    is_tenant = models.BooleanField(default=True)
    is_landlord = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Soft delete
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'em_users_users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def delete(self, using = None, keep_parents = False):
        self.is_active = False
        self.is_deleted = True
        self.deleted_at = timezone.now()
        return self.save(update_fields=['is_deleted', 'deleted_at'])
