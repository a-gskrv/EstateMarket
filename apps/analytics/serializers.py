from rest_framework import serializers

from apps.listings.models import Listing


# from apps.listings.serializers import  PropertyListSerializer


class TopListingViewSerializer(serializers.ModelSerializer):
    views_count = serializers.IntegerField(read_only=True)

    # property = PropertyListSerializer(read_only=True)
    class Meta:
        model = Listing
        fields = (
            'views_count',
            'id',
            'title',
            'price',
            # 'property',
        )


class TopListingReviewsSerializer(serializers.ModelSerializer):
    reviews_count = serializers.IntegerField(read_only=True)

    # property = PropertyListSerializer(read_only=True)
    class Meta:
        model = Listing
        fields = (
            'reviews_count',
            'id',
            'title',
            'price',
            # 'property',
        )
