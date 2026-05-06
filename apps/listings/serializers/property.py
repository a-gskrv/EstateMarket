from rest_framework import serializers

from apps.listings.models import Property, PropertyType
from apps.listings.serializers.location import LocationDetailSerializer


class PropertyTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = [
            'id',
            'name',
        ]


class PropertyTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = "__all__"


class PropertyListSerializer(serializers.ModelSerializer):
    location = LocationDetailSerializer(read_only=True)

    class Meta:
        model = Property
        fields = [
            'id',
            'title',
            'location',
            'rooms_count',
            'sleeping_places',
        ]


class PropertyDetailSerializer(serializers.ModelSerializer):
    location = LocationDetailSerializer(read_only=True)
    property_type = PropertyTypeListSerializer(read_only=True)

    class Meta:
        model = Property
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class PropertyCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"
