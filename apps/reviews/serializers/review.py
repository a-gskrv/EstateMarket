from rest_framework import serializers

from apps.bookings.serializers import BookingShortListSerializer
from apps.reviews.models.review import Review
from apps.users.serializers import UserShortSerializer


class ReviewListSerializer(serializers.ModelSerializer):
    short_review_text = serializers.SerializerMethodField()
    user = UserShortSerializer(read_only=True)
    booking = BookingShortListSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'booking',
            'user',
            'rating',
            'short_review_text',
            'created_at',
            'updated_at',
        ]

    def get_short_review_text(self, obj):
        if len(obj.review_text) > 100:
            return f"{obj.review_text[:96]} ..."
        return obj.review_text

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user

        booking = attrs.get('booking')
        tenant = booking.tenant
        is_tenant_checked_in = booking.is_tenant_checked_in

        if user != tenant:
            raise serializers.ValidationError(
                'You can review only your own booking.'
            )
        if is_tenant_checked_in == False:
            raise serializers.ValidationError(
                'You can leave a review only after check-in.'
            )

        return attrs



