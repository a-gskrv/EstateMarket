from rest_framework.permissions import BasePermission


class IsLandlord(BasePermission):
    message = "Only landlords can perform this action."
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_landlord
        )


class IsTenant(BasePermission):
    message = "Only landlords can perform this action."
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_tenant
        )

class IsLandlordOrAdmin(BasePermission):
    message = "Only landlords can perform this action."
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            (request.user.is_superuser or request.user.is_landlord)
        )