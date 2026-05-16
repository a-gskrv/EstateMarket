from django.db import models
from django.db.models import Q
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.bookings.models import Booking, BookingStatus
from apps.bookings.permissions import IsBookingOwner, IsBookingPropertyOwner
from apps.bookings.serializers import (
    BookingListSerializer,
    BookingDetailSerializer,
    BookingUpdateStatusSerializer,
    BookingCreateSerializer,
    BookingChangeDateSerializer
)

from apps.core.permissions import IsTenant
from apps.users.permissions import IsAdmin


class BookingViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        user = self.request.user

        if user and user.is_authenticated and user.is_superuser:
            return Booking.objects.all()

        queryset = Booking.objects.all()
        queryset = queryset.filter(is_active=True)
        queryset = queryset.filter(
            Q(tenant=user) |
            Q(listing__property__owner=user)
        )
        return queryset

    def get_serializer_class(self):
        # if self.action in ('update', 'partial_update'):
        #     return BookingDetailSerializer
        # elif self.action == 'create':
        #     return BookingCreateSerializer

        if self.action in ('partial_update'):
            return BookingChangeDateSerializer
            ...
        elif self.action in ('status_confirmed', 'status_rejected'):
            ...
        elif self.action in ('status_cancelled'):
            ...

        return BookingListSerializer

    def get_permissions(self):

        print('get_permissions', self.request.user, self.action, self.request.method)
        if self.action in ('create', 'partial_update', 'status_pending', 'status_cancelled'):
            permission_classes = [IsTenant | IsAdmin]
        elif self.action in ('status_confirmed', 'status_rejected'):
            permission_classes = [IsBookingPropertyOwner | IsAdmin]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.validated_data['tenant'] = self.request.user
        super().perform_create(serializer)

    @action(
        detail=True,
        methods=['post'],
        # methods=['post', 'get'],
        url_name='pending'
    )
    def status_pending(self, request, pk=None):
        obj = self.get_object()

        obj.booking_status = BookingStatus.PENDING
        obj.save(update_fields=["booking_status", 'updated_at'])
        serializer = BookingUpdateStatusSerializer(obj)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    @action(
        detail=True,
        methods=['post'],
        # methods=['post', 'get'],
        url_name='confirmed'
    )
    def status_confirmed(self, request, pk=None):
        obj = self.get_object()

        obj.booking_status = BookingStatus.CONFIRMED
        obj.confirmed_at = timezone.now()

        obj.save(update_fields=["booking_status", 'updated_at', 'confirmed_at'])
        serializer = BookingUpdateStatusSerializer(obj)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    @action(
        detail=True,
        methods=['post'],
        # methods=['post', 'get'],
        url_name='cancelled'
    )
    def status_cancelled(self, request, pk=None):
        obj = self.get_object()

        obj.booking_status = BookingStatus.CANCELLED
        obj.save(update_fields=["booking_status", 'updated_at'])
        serializer = BookingUpdateStatusSerializer(obj)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    @action(
        detail=True,
        methods=['post'],
        # methods=['post', 'get'],
        url_name='completed'
    )
    def status_completed(self, request, pk=None):
        obj = self.get_object()

        obj.booking_status = BookingStatus.COMPLETED
        obj.is_tenant_checked_in = True
        actual_end_date = request.data.get('actual_end_date')
        if not actual_end_date:
            obj.actual_end_date = timezone.now().date()
        else:
            obj.actual_end_date = actual_end_date

        obj.save(update_fields=[
            "booking_status",
            'updated_at',
            'is_tenant_checked_in',
            'actual_end_date',
        ])
        serializer = BookingUpdateStatusSerializer(obj)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    @action(
        detail=True,
        methods=['post'],
        # methods=['post', 'get'],
        url_name='rejected'
    )
    def status_rejected(self, request, pk=None):
        obj = self.get_object()

        obj.booking_status = BookingStatus.REJECTED
        obj.save(update_fields=["booking_status", 'updated_at'])
        serializer = BookingUpdateStatusSerializer(obj)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )


"""
    PENDING = 0, "Pending"          # Ожидает подтверждения
    CONFIRMED = 1, "Confirmed"      # Подтверждено
    CANCELLED = 2, "Cancelled"      # Отменено
    COMPLETED = 3, "Completed"      # Завершено
    REJECTED = 4, "Rejected"        # Отклонено
"""
