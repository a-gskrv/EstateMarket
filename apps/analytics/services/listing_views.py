from datetime import timedelta

from django.utils import timezone

from apps.analytics.models import ListingView
from apps.listings.models import Listing
from apps.users.models import User


def register_listing_view(
        listing: Listing,
        user: User = None,
        guest_ip: str = None,
        guest_agent: str = None,
):
    if is_unique_listing_view(listing, user, guest_ip, guest_agent):
        try:
            ListingView.objects.create(
                listing=listing,
                user=user,
                guest_ip=guest_ip,
                guest_agent=guest_agent,
            )

        except Exception as e:
            print(e)


def is_unique_listing_view(listing: Listing, user, guest_ip, guest_agent):
    period_start = timezone.now() - timedelta(days=1)
    if user and user.is_authenticated:
        already_exists = ListingView.objects.filter(
            listing=listing,
            user=user,
            created_at__gte=period_start,
        ).exists()
    else:
        already_exists = ListingView.objects.filter(
            listing=listing,
            user=None,
            guest_ip=guest_ip,
            guest_agent=guest_agent,
            created_at__gte=period_start,
        ).exists()

    return not already_exists
