from django.db.models import Q
from django.db.models.functions import Coalesce

from apps.bookings.models import BookingStatus, Booking


def check_booking_availability(listing,
                               booking_start_date,
                               booking_end_date, ):
    qs = Booking.objects.filter(listing__property=listing.property)
    qs = qs.annotate(
        effective_end_date=Coalesce(
            "actual_end_date",
            "booking_end_date"
        )
    )

    qs = qs.filter(
        booking_start_date__lt=booking_end_date,
        effective_end_date__gt=booking_start_date,

    )
    qs = qs.filter(
        booking_status__in=
        [BookingStatus.PENDING,
         BookingStatus.CONFIRMED]
    )

    return not qs.exists()
