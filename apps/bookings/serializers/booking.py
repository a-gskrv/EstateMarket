from rest_framework import serializers

from apps.bookings.models import Booking
from apps.listings.serializers import LocationDetailSerializer, ListingDetailSerializer, ListingListSerializer
from apps.users.serializers import UserShortSerializer


class BookingShortListSerializer(serializers.ModelSerializer):
    listing = ListingListSerializer(read_only=True)
    user = UserShortSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = [
            'id',
            'user',
            'listing',
            'booking_start_date',
            'booking_end_date',
            'booking_amount',
            'booking_status',
            'is_tenant_checked_in',
        ]

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

        read_only_fields = [
            'id',
            'listing',
            'tenant',
            'confirmed_at',
            'booking_amount',
            'booking_status',
            'is_tenant_checked_in',

            'is_active',
            'created_at',
            'updated_at',
            'is_deleted',
            'deleted_at',

        ]

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user

        listing = attrs.get('listing')
        owner = listing.property.owner

        if user == owner:
            raise serializers.ValidationError(
                'You cannot create a booking for your own listing.'
            )

        return attrs


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