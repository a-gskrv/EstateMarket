from rest_framework import serializers

from apps.bookings.models import Booking
from apps.listings.serializers import LocationDetailSerializer, ListingDetailSerializer
from apps.users.serializers import UserShortSerializer


class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id',
            'listing',
            'tenant',
            'confirmed_at',
            'booking_start_date',
            'booking_end_date',
            'booking_amount',
            'booking_status',
            'is_tenant_checked_in',

            'is_active',
            'created_at',
            'updated_at',
            'is_deleted',
            'deleted_at',
        ]


class BookingListSerializer(serializers.ModelSerializer):
    listing = ListingDetailSerializer(read_only=True)
    tenant = UserShortSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id',
            'listing',
            'tenant',
            'confirmed_at',
            'booking_start_date',
            'booking_end_date',
            'booking_amount',
            'booking_status',
            'is_tenant_checked_in',
            'is_active',
            'created_at',
            'updated_at',
            'is_deleted',
            'deleted_at',
        ]

class BookingUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id',
            'confirmed_at',
            'booking_status',
            'is_tenant_checked_in',
            'updated_at',
        ]