from django.db import models
from django.utils import timezone


class Listing(models.Model):
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
        db_table = 'em_listings_listing'
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.is_deleted = True
        self.deleted_at = timezone.now()
        return self.save(update_fields=['is_active', 'is_deleted', 'deleted_at'])
