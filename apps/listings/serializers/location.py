from rest_framework import serializers

from apps.listings.models.location import Location


class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            "id",
            "title",
            "display_description",
        ]