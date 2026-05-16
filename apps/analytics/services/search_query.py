from datetime import timedelta

from django.utils import timezone

from apps.analytics.models import SearchQuery
from apps.users.models import User


def register_search_query(
        query: str,
        user: User = None,
        guest_ip: str = None,
        guest_agent: str = None,
):
    lower_query = query.lower().strip()
    if is_unique_search_query(lower_query, user, guest_ip, guest_agent):
        try:
            SearchQuery.objects.create(
                query=lower_query,
                user=user,
                guest_ip=guest_ip,
                guest_agent=guest_agent,
            )

        except Exception as e:
            print(e)


def is_unique_search_query(query: str, user, guest_ip, guest_agent):
    period_start = timezone.now() - timedelta(days=1)
    if user and user.is_authenticated:
        already_exists = SearchQuery.objects.filter(
            query=query,
            user=user,
            created_at__gte=period_start,
        ).exists()
    else:
        already_exists = SearchQuery.objects.filter(
            query=query,
            user=None,
            guest_ip=guest_ip,
            guest_agent=guest_agent,
            created_at__gte=period_start,
        ).exists()

    return not already_exists
