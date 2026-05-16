from django.db import models

from apps.core.base_models import ActiveSoftDeleteModel, TimeStampedModel


class Location(ActiveSoftDeleteModel, TimeStampedModel):
    postal_code = models.CharField(max_length=7)
    country = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)

    house_number = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )

    extra_info = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    display_description = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = 'em_listings_location'
        verbose_name = 'Location'
        verbose_name_plural = "Locations"

    def __str__(self):
        if self.display_description:
            return self.display_description

        parts = [
            self.street,
            self.house_number,
            self.city,
            self.country,
        ]

        display_description = ", ".join([part for part in parts if part])
        return display_description
