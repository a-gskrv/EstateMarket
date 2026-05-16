from rest_framework import viewsets

from apps.reviews.models.review import Review
from apps.reviews.permissions import IsBookingTenantOrReadOnly
from apps.reviews.serializers import ReviewListSerializer, ReviewDetailSerializer, ReviewCreateSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()

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
