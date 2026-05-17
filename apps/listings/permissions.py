from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsListingOwnerOrReadOnly(BasePermission):
    message = "You do not have permission to manage this listing."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user and
            request.user.is_authenticated and
            (
                    request.user.is_superuser or
                    request.user.is_landlord
            )
        )

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user and
            request.user.is_authenticated and
            (
                    request.user.is_superuser or
                    obj.property.owner == request.user
            )
        )


class IsPropertyOwnerOrReadOnly(BasePermission):
    message = "You do not have permission to manage this property."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user and
            request.user.is_authenticated and
            (
                request.user.is_superuser or
                request.user.is_landlord
            )
        )


    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # elif request.method in ['PUT', 'PATCH', 'DELETE']:
        return bool(
            request.user and
            request.user.is_authenticated and
            (
                    request.user.is_superuser or
                    obj.owner == request.user
            )
        )


# class IsListingOwner(BasePermission):
#     message = "Only the listing owner can perform this action."
#     def has_object_permission(self, request, view, obj):
#         return bool(
#             request.user and
#             request.user.is_authenticated and
#             obj.property.owner == request.user
#         )
#
# class IsPropertyOwner(BasePermission):
#     message = "Only the property owner can perform this action."
#     def has_object_permission(self, request, view, obj):
#         return bool(
#             request.user and
#             request.user.is_authenticated and
#             obj.owner == request.user
#         )