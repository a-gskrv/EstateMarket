from django.db import models


class ListingView(models.Model):
    listing = models.ForeignKey(
        'listings.Listing',
        on_delete=models.CASCADE,
        related_name='views_',
    )

    user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='listing_views'
    )

    guest_id = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'em_analytics_listing_view'
        verbose_name = 'Listing View'
        verbose_name_plural = 'Listing Views'
        ordering = ['-created_at']
