from datetime import timedelta

from django.db.models import Count, Q
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.analytics.serializers import TopListingViewSerializer
from apps.listings.models import Listing


class AnalyticsView(APIView):

    def get(self, request, *args, **kwargs):

        days = request.query_params.get('days')
        count = request.query_params.get('count')

        top_listing_view = Listing.objects.all().filter(is_active=True)
        if days and days.isdigit() and int(days)>0:
            period_start = timezone.now() - timedelta(days=int(days))
        else:
            period_start = timezone.now() - timedelta(days=90)

        top_listing_view = top_listing_view.annotate(
            views_count=Count(
                'views',
                filter=Q(views__created_at__gte=period_start)
            )
        )

        top_listing_view = top_listing_view.order_by('-views_count')

        if count and count.isdigit() and int(count)>0:
            top_listing_view = top_listing_view[:int(count)]
        else:
            top_listing_view = top_listing_view[:100]

        serializer = TopListingViewSerializer(top_listing_view, many=True)



        return Response({
            'top_listing_view': serializer.data,
        })


