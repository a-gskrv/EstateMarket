from django.utils import timezone

from rest_framework import viewsets

from apps.listings.models import Listing, Property, PropertyType
from apps.listings.permissions import IsListingOwnerOrReadOnly, IsPropertyOwnerOrReadOnly

from apps.listings.serializers.property import (
    PropertyListSerializer,
    PropertyDetailSerializer,

    PropertyTypeDetailSerializer,
    PropertyTypeListSerializer,
    PropertyCreateUpdateSerializer,
)
from apps.users.permissions import IsAdmin, IsAdminOrReadOnly


class PropertyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPropertyOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if not user or not user.is_authenticated:
            return Property.active_objects.none()

        if user.is_superuser:
            return Property.objects.all()

        return Property.active_objects.all().filter(owner=user)



    def get_serializer_class(self):
        if self.action == "list":
            return PropertyListSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return PropertyCreateUpdateSerializer

        return PropertyDetailSerializer

        # def get_permissions(self):
        #     if self.action == 'create':
        #         permission_classes = [
        #             # IsAuthenticated,
        #             IsLandlord | IsAdmin
        #         ]
        #     elif self.action  in ["update", "partial_update", "destroy"]:
        #         permission_classes = [
        #             # IsAuthenticated,
        #             IsPropertyOwner | IsAdmin]
        #
        #     else:
        #         permission_classes = [AllowAny]

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


class PropertyTypeViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None


    def get_queryset(self):
        user = self.request.user

        if user and user.is_authenticated and user.is_superuser:
            return PropertyType.objects.all().order_by("name")

        return PropertyType.active_objects.all().order_by("name")

    def get_serializer_class(self):
        if self.action == "list":
            return PropertyTypeListSerializer

        return PropertyTypeDetailSerializer
