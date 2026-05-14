from django.utils import timezone
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions import IsLandlord
from apps.listings.models import Listing, Property, PropertyType
from apps.listings.permissions import IsPropertyOwner

from apps.listings.serializers.property import (
    PropertyListSerializer,
    PropertyDetailSerializer,

    PropertyTypeDetailSerializer,
    PropertyTypeListSerializer,
    PropertyCreateUpdateSerializer,
)
from apps.users.permissions import IsAdmin


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return PropertyListSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return PropertyCreateUpdateSerializer

        return PropertyDetailSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [
                # IsAuthenticated,
                IsLandlord | IsAdmin
            ]
        elif self.action  in ["update", "partial_update", "destroy"]:
            permission_classes = [
                # IsAuthenticated,
                IsPropertyOwner | IsAdmin]

        else:
            permission_classes = [AllowAny]


        return [permission() for permission in permission_classes]

    # def perform_destroy(self, instance):
    #     instance.is_active = False
    #     instance.is_deleted = True
    #     instance.deleted_at = timezone.now()
    #     return instance.save(
    #         update_fields=[
    #             'is_active',
    #             'is_deleted',
    #             'deleted_at'
    #         ]
    #     )


class PropertyTypeViewSet(ModelViewSet):
    queryset = PropertyType.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return PropertyTypeListSerializer

        return PropertyTypeDetailSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.deleted_at = timezone.now()
        return instance.save(
            update_fields=[
                'is_deleted',
                'deleted_at'
            ]
        )
