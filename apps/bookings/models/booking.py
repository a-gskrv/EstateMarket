from django.db import models

from apps.core.base_models import TimeStampedModel, ActiveSoftDeleteModel


class BookingStatus(models.IntegerChoices):
    PENDING = 0, "Pending"
    CONFIRMED = 1, "Confirmed"
    CANCELLED = 2, "Cancelled"
    COMPLETED = 3, "Completed"
    REJECTED = 4, "Rejected"


class Booking(TimeStampedModel, ActiveSoftDeleteModel):
    listing = models.ForeignKey(
        'listings.Listing',
        on_delete=models.RESTRICT,
        related_name="bookings",
    )

    tenant = models.ForeignKey(
        'users.User',
        on_delete=models.RESTRICT,
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
    actual_end_date = models.DateField(
        null=True,
        blank=True,
        default=None
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

    class Meta:
        db_table = "em_bookings_booking"
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"{self.id}. {self.tenant}: {self.listing.title} -> ({self.booking_start_date} - {self.booking_end_date})"
