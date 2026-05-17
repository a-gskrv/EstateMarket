from django.db import models


class NotDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_deleted=False,
        )


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_active=True,
        )


class ActiveNotDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_active=True,
            is_deleted=False,
        )
