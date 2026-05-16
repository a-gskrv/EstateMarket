from django.db import models
from django.utils import timezone

from apps.core.managers import ActiveManager, ActiveNotDeletedManager, NotDeletedManager


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = NotDeletedManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        if not self.is_deleted:
            self.is_deleted = True
            self.deleted_at = timezone.now()
            return self.save(update_fields=['is_deleted', 'deleted_at'])
        return self

    def hard_delete(self, using=None, keep_parents=False):
        return super().delete(using=using, keep_parents=keep_parents)


class ActiveModel(models.Model):
    is_active = models.BooleanField(default=True)

    objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True


class ActiveSoftDeleteModel(SoftDeleteModel):
    is_active = models.BooleanField(default=True)

    objects = ActiveNotDeletedManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True
