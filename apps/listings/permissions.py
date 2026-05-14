from rest_framework.permissions import BasePermission


class IsListingOwner(BasePermission):
    message = "Only the listing owner can perform this action."
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user.is_authenticated and
            obj.property.owner == request.user
        )