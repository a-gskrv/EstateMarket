from django.utils import timezone
from rest_framework.viewsets import ModelViewSet

from apps.listings.models import Listing, Property
from apps.listings.serializers.listing import (
    ListingListSerializer,
    ListingDetailSerializer,
    ListingCreateUpdateSerializer
)


class ListingViewSet(ModelViewSet):
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
