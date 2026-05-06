from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


USER_MODEL = get_user_model()

class Review(models.Model):
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
        db_table = "em_reviews_review"
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"{self.user}: {self.rating} -> ({self.booking.listing.title})"

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.is_deleted = True
        self.deleted_at = timezone.now()
        return self.save(update_fields=['is_active', 'is_deleted', 'deleted_at'])
