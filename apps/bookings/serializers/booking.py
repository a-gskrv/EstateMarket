from datetime import timedelta

from django.utils import timezone
from rest_framework import serializers

from apps.bookings.models import Booking
from apps.bookings.utils import check_booking_availability
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
            'actual_end_date',
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
        fields = [
            'listing',
            'tenant',
            'booking_start_date',
            'booking_end_date',
            'booking_amount'
        ]
        read_only_fields = [
            'tenant',
            'booking_amount'

        ]

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user

        listing = attrs.get('listing')
        owner = listing.property.owner
        print("#"*60)
        print(listing, owner)

        if user == owner:
            raise serializers.ValidationError(
                'You cannot create a booking for your own listing.'
            )

        booking_end_date = attrs.get('booking_end_date')
        booking_start_date = attrs.get('booking_start_date')

        if booking_start_date >= booking_end_date:
            raise serializers.ValidationError(
                'Booking start date must be before booking end date.'
            )



        is_listing_available = check_booking_availability(
            listing,
            booking_start_date,
            booking_end_date,
        )

        if not is_listing_available:
            raise serializers.ValidationError(
                "This listing is not available for the selected dates."
            )

        count_days = (booking_end_date - booking_start_date).days
        attrs['booking_amount'] = count_days * listing.price
        print(attrs.get('booking_amount'))



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
            'actual_end_date',
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
            'actual_end_date'
        ]
        read_only_fields = [
            'id',
            'confirmed_at',
            'is_tenant_checked_in',
            'updated_at',
            'actual_end_date'
        ]

class BookingChangeDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'booking_start_date',
            'booking_end_date',
        ]

    def validate(self, attrs):
        max_cancel_day = 2
        max_date_change = timezone.now().date() + timedelta(days=max_cancel_day)

        old_booking_start_date = self.instance.booking_start_date

        booking_start_date = attrs.get('booking_start_date')
        booking_end_date = attrs.get('booking_end_date')

        if max_date_change > old_booking_start_date:
            raise serializers.ValidationError(
                'Booking dates can no longer be changed before check-in.'
            )

        if booking_start_date > booking_end_date:
            raise serializers.ValidationError(
                'Booking end date must be later than booking start date.'
            )

        return attrs