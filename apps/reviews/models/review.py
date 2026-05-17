from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from apps.core.base_models import ActiveSoftDeleteModel, TimeStampedModel

USER_MODEL = get_user_model()

class Review(ActiveSoftDeleteModel, TimeStampedModel):
    booking = models.ForeignKey(
        "bookings.Booking",
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
    )

    review_text = models.TextField()

    class Meta:
        db_table = "em_reviews_review"
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

        constraints = [
            models.UniqueConstraint(
                fields=["booking", "user"],
                name="unique_review_per_booking_user",
            )
        ]

    def __str__(self):
        return f"{self.user}: {self.rating} -> ({self.booking.listing.title})"
