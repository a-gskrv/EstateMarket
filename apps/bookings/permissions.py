from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps import permissions







class IsNotListingOwner(BasePermission):
    message = "You cannot book your own listing."

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user.is_authenticated and
            obj.listing.property.owner != request.user
        )


class IsBookingOwner(BasePermission):
    message = "Only the booking owner can perform this action."

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user.is_authenticated and
            obj.tenant == request.user
        )



class IsBookingOwnerOrReadOnly(BasePermission):
    message = "Only the booking owner can perform this action."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.teant == request.user
