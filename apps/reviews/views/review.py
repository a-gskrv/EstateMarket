from rest_framework import viewsets

from apps.reviews.models.review import Review
from apps.reviews.permissions import IsBookingTenantOrReadOnly
from apps.reviews.serializers import ReviewListSerializer, ReviewDetailSerializer, ReviewCreateSerializer


class ReviewViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        user = self.request.user

        if user and user.is_authenticated and user.is_superuser:
            return Review.all_objects.all()

        return Review.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ReviewListSerializer
        if self.action == "create":
            return ReviewCreateSerializer

        return ReviewDetailSerializer

    def get_permissions(self):
        return [IsBookingTenantOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
