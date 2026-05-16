from django.db import models
from django.utils import timezone

from apps.core.base_models import ActiveSoftDeleteModel, TimeStampedModel


class Listing(ActiveSoftDeleteModel, TimeStampedModel):
    title = models.CharField(
        max_length=150,
    )
    property = models.ForeignKey(
        "listings.Property",
        on_delete=models.CASCADE,
        related_name="listings",
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    settlement_conditions = models.TextField(
        blank=True,
        null=True,
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = 'em_listings_listing'
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'

    def __str__(self):
        return self.title
