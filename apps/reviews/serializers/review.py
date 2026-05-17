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
        fields = [
            'booking',
            'user',
            'rating',
            'review_text',
        ]
        read_only_fields = ['user']

    def validate(self, attrs):
        print('validate', attrs)

        request = self.context.get('request')
        user = request.user
        print(user)

        booking = attrs.get('booking')

        if not booking:
            raise serializers.ValidationError(
                {"booking": "Booking is required."}
            )

        if Review.objects.filter(booking=booking, user=user).exists():
            print(booking, user)
            raise serializers.ValidationError(
                "You have already reviewed this booking."
            )

        tenant = booking.tenant

        if user != tenant:
            raise serializers.ValidationError(
                'You can review only your own booking.'
            )
        if not booking.is_tenant_checked_in:
            raise serializers.ValidationError(
                'You can leave a review only after staying at the property.'
            )

        return attrs
