from datetime import timedelta

from django.db.models import Count, Q
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.analytics.models import SearchQuery
from apps.analytics.serializers import TopListingViewSerializer, TopListingReviewsSerializer, TopSearchQuerySerializer
from apps.listings.models import Listing


class AnalyticsView(APIView):

    def get(self, request, *args, **kwargs):

        days = request.query_params.get('days')
        count = request.query_params.get('count')


        if days and days.isdigit() and int(days) > 0:
            period_start = timezone.now() - timedelta(days=int(days))
        else:
            period_start = timezone.now() - timedelta(days=90)


        if count and count.isdigit() and int(count) > 0:
            count = int(count)

        else:
            count = None

        top_listing_view = get_top_listing_view(period_start, count)
        top_listing_reviews = get_top_listing_reviews(period_start, count)
        top_search_query = get_top_search_query(period_start, count)

        return Response({
            'top_listing_view': top_listing_view,
            'top_listing_reviews': top_listing_reviews,
            'top_search_query': top_search_query,
        })


def get_top_listing_view(period_start=None, count=None):

    top_listing = Listing.objects.all().filter(is_active=True)

    if period_start:
        filter_date = Q(views__created_at__gte=period_start)
    else:
        filter_date = Q()

    top_listing = top_listing.annotate(
        views_count=Count(
            'views',
            filter=filter_date
        )
    )

    if count:
        top_listing_view = top_listing[:int(count)]

    top_listing = top_listing.order_by('-views_count')
    serializer = TopListingViewSerializer(top_listing, many=True)
    return serializer.data


def get_top_listing_reviews(period_start=None, count=None):

    top_listing = Listing.objects.all().filter(is_active=True)

    if period_start:
        filter_date = Q(bookings__reviews__created_at__gte=period_start)
    else:
        filter_date = Q()

    print(period_start)

    top_listing = top_listing.annotate(
        reviews_count=Count(
            'bookings__reviews',
            filter=filter_date
        )
    )

    top_listing = top_listing.order_by('-reviews_count')
    if count:
        top_listing = top_listing[:int(count)]

    serializer = TopListingReviewsSerializer(top_listing, many=True)
    return serializer.data


def get_top_search_query(period_start = None, count = 10):

    top_query = SearchQuery.objects.all()

    if period_start:
        filter_date = Q(created_at__gte=period_start)


    top_query = (
        top_query
        .values('query')
        .annotate(search_count=Count('id'))
        .order_by('-search_count', '-created_at')[:count]
    )

    serializer = TopSearchQuerySerializer(top_query, many=True)
    return serializer.data