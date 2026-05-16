from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsBookingTenantOrReadOnly(BasePermission):
    message = "Only tenants who completed the booking can manage reviews."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.user and
            request.user.is_authenticated and
            (request.user.is_tenant or request.user.is_superuser)
        )

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user
            and request.user.is_authenticated
            and (
                    request.user.is_superuser
                    or (
                            obj.booking.tenant == request.user
                            and obj.booking.is_tenant_checked_in
                    )
            )
        )
