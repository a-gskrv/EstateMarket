from django.db import models
from django.utils import timezone


class Location(models.Model):
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

    #
    # def delete(self, using=None, keep_parents=False):
    #     self.is_active = False
    #     self.is_deleted = True
    #     self.deleted_at = timezone.now()
    #     return self.save(update_fields=['is_active', 'is_deleted', 'deleted_at'])
