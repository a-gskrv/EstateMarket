from django.db import models
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.bookings.models import Booking, BookingStatus
from apps.bookings.serializers import BookingListSerializer, BookingDetailSerializer
from apps.bookings.serializers.booking import BookingUpdateStatusSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return BookingDetailSerializer

        return BookingListSerializer


    @action(
        detail=True,
        methods=['post'],
        # methods=['post', 'get'],
        url_name='pending'
    )
    def status_pending(self, request, pk=None):
        obj = self.get_object()
        r_user = request.user


        if bool(
                r_user and
                r_user.is_authenticated and
                r_user.is_superuser
        ) or bool(
            r_user and
            r_user.id == obj.listing.property.owner.id
        ):

            obj.booking_status = BookingStatus.PENDING
            obj.save(update_fields=["booking_status", 'updated_at'])
            serializer = BookingUpdateStatusSerializer(obj)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data='You do not have permission to perform this action.',
            status=status.HTTP_403_FORBIDDEN
        )



    @action(
        detail=True,
        methods=['post'],
        # methods=['post', 'get'],
        url_name='confirmed'
    )
    def status_confirmed(self, request, pk=None):
        obj = self.get_object()
        r_user = request.user

        if bool(
                r_user and
                r_user.is_authenticated and
                r_user.is_superuser
        ) or bool(
            r_user and
            r_user.id == obj.listing.property.owner.id
        ):

            obj.booking_status = BookingStatus.CONFIRMED
            obj.save(update_fields=["booking_status", 'updated_at'])
            serializer = BookingUpdateStatusSerializer(obj)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data='You do not have permission to perform this action.',
            status=status.HTTP_403_FORBIDDEN
        )

    @action(
        detail=True,
        methods=['post'],
        # methods=['post', 'get'],
        url_name='cancelled'
    )
    def status_cancelled(self, request, pk=None):
        obj = self.get_object()
        r_user = request.user


        if bool(
                r_user and
                r_user.is_authenticated and
                r_user.is_superuser
        ) or bool(
            r_user and
            r_user.id == obj.listing.property.owner.id
        ):

            obj.booking_status = BookingStatus.CANCELLED
            obj.save(update_fields=["booking_status", 'updated_at'])
            serializer = BookingUpdateStatusSerializer(obj)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data='You do not have permission to perform this action.',
            status=status.HTTP_403_FORBIDDEN
        )


    @action(
        detail=True,
        methods=['post'],
        # methods=['post', 'get'],
        url_name='completed'
    )
    def status_completed(self, request, pk=None):
        obj = self.get_object()
        r_user = request.user


        if bool(
                r_user and
                r_user.is_authenticated and
                r_user.is_superuser
        ) or bool(
            r_user and
            r_user.id == obj.listing.property.owner.id
        ):

            obj.booking_status = BookingStatus.COMPLETED
            obj.save(update_fields=["booking_status", 'updated_at'])
            serializer = BookingUpdateStatusSerializer(obj)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data='You do not have permission to perform this action.',
            status=status.HTTP_403_FORBIDDEN
        )


    @action(
        detail=True,
        methods=['post'],
        # methods=['post', 'get'],
        url_name='rejected'
    )
    def status_rejected(self, request, pk=None):
        obj = self.get_object()
        r_user = request.user


        if bool(
                r_user and
                r_user.is_authenticated and
                r_user.is_superuser
        ) or bool(
            r_user and
            r_user.id == obj.listing.property.owner.id
        ):

            obj.booking_status = BookingStatus.REJECTED
            obj.save(update_fields=["booking_status", 'updated_at'])
            serializer = BookingUpdateStatusSerializer(obj)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data='You do not have permission to perform this action.',
            status=status.HTTP_403_FORBIDDEN
        )



"""
    PENDING = 0, "Pending"
    CONFIRMED = 1, "Confirmed"
    CANCELLED = 2, "Cancelled"
    COMPLETED = 3, "Completed"
    REJECTED = 4, "Rejected"
"""