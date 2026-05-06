from rest_framework import serializers

from apps.listings.models import Listing
from apps.listings.serializers.location import LocationDetailSerializer
from apps.listings.serializers.property import PropertyTypeListSerializer, PropertyDetailSerializer


class ListingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'id',
            'title', ]

class ListingDetailSerializer(serializers.ModelSerializer):
    location = LocationDetailSerializer(read_only=True)
    property_type = PropertyTypeListSerializer(read_only=True)
    property = PropertyDetailSerializer(read_only=True)
    class Meta:
        model = Listing
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

class ListingCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"
        # read_only_fields = [
        #     "id",
        #     "created_at",
        #     "updated_at",
        # ]