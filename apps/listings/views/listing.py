import django_filters
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.analytics.services.listing_views import register_listing_view
from apps.analytics.services.search_query import register_search_query
from apps.listings.filters import ListingFilter
from apps.listings.models import Listing, Property
from apps.listings.serializers.listing import (
    ListingListSerializer,
    ListingDetailSerializer,
    ListingCreateUpdateSerializer
)


class ListingViewSet(ModelViewSet):
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )

    filterset_class = ListingFilter

    # filterset_fields = (
    #     'price',
    #     'property__location__region',
    #     'property__location__city',
    #     'property__rooms_count',
    #     'property__property_type',
    # )

    search_fields = (
        'title',
        'property__description',
    )

    ordering_fields = (
        'price',
        'created_at',
        'updated_at',
    )

    #selectrelated  &  prefetch_related()
    queryset = Listing.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ListingListSerializer
        if self.action in ('create', 'update', 'partial_update'):
            return ListingCreateUpdateSerializer

        return ListingDetailSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.is_deleted = True
        instance.deleted_at = timezone.now()
        return instance.save(
            update_fields=[
                'is_active',
                'is_deleted',
                'deleted_at'
            ]
        )

    def retrieve(self, request, *args, **kwargs):
        try:
            listing = self.get_object()
            if request.user and request.user.is_authenticated:
                user = request.user
            else:
                user = None
            guest_ip = request.META.get('REMOTE_ADDR')
            guest_agent = request.META.get('HTTP_USER_AGENT')

            register_listing_view(
                listing=listing,
                user=user,
                guest_ip=guest_ip,
                guest_agent=guest_agent
            )


        except Exception as e:
            print(e)

        return super().retrieve(self, request, *args, **kwargs)


    def list(self, request, *args, **kwargs):
        try:
            search = request.query_params.get('search')
            if search:

                if request.user and request.user.is_authenticated:
                    user = request.user
                else:
                    user = None
                guest_ip = request.META.get('REMOTE_ADDR')
                guest_agent = request.META.get('HTTP_USER_AGENT')

                register_search_query(
                    query=search,
                    user=user,
                    guest_ip=guest_ip,
                    guest_agent=guest_agent
                )


        except Exception as e:
            print(e)


        return super().list(self, request, *args, **kwargs)
