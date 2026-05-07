from django.db import models
from django.utils import timezone

from apps.users.models import User


class PropertyType(models.Model):
    name = models.CharField(max_length=30)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'em_listings_property_type'
        verbose_name = 'Property Type'
        verbose_name_plural = "Property Types"

    def __str__(self):
        return self.name


class Property(models.Model):
    title = models.CharField(
        max_length=50,
    )
    property_type = models.ForeignKey(
        'PropertyType',
        on_delete=models.RESTRICT,
        related_name="properties",
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    location = models.ForeignKey(
        "listings.Location",
        on_delete=models.RESTRICT,
        related_name="properties",
    )

    area = models.PositiveSmallIntegerField()
    rooms_count = models.PositiveSmallIntegerField()
    sleeping_places = models.PositiveSmallIntegerField()

    owner = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name="properties",
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "em_listings_property"
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.is_deleted = True
        self.deleted_at = timezone.now()
        return self.save(update_fields=['is_active', 'is_deleted', 'deleted_at'])
