from django.db import models
from django.utils import timezone

from listings.models import Listing
from users.models import User


class BookingStatus(models.IntegerChoices):
    PENDING = 0, "Pending"
    CONFIRMED = 1, "Confirmed"
    CANCELLED = 2, "Cancelled"
    COMPLETED = 3, "Completed"
    REJECTED = 4, "Rejected"


class Booking(models.Model):
    listing = models.ForeignKey(
        Listing,
        on_delete=models.PROTECT,
        related_name="bookings",
    )

    tenant = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="bookings",
    )

    confirmed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    booking_start_date = models.DateField(
        null=True,
        blank=True,
    )
    booking_end_date = models.DateField(
        null=True,
        blank=True,
    )
    booking_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    booking_status = models.IntegerField(
        choices=BookingStatus.choices,
        default=BookingStatus.PENDING,
    )

    is_tenant_checked_in = models.BooleanField(default=False)

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
        db_table = "bookings_booking"
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"{self.tenant}: {self.listing.title} -> ({self.booking_start_date} - {self.booking_end_date})"

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.is_deleted = True
        self.deleted_at = timezone.now()
        return self.save(update_fields=['is_active', 'is_deleted', 'deleted_at'])
