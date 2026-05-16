from django.db import models
from django.utils import timezone

from apps.core.base_models import SoftDeleteModel, ActiveSoftDeleteModel, TimeStampedModel
from apps.users.models import User


class PropertyType(SoftDeleteModel):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'em_listings_property_type'
        verbose_name = 'Property Type'
        verbose_name_plural = "Property Types"

    def __str__(self):
        return self.name


class Property(ActiveSoftDeleteModel, TimeStampedModel):
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


    class Meta:
        db_table = "em_listings_property"
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title
