from rest_framework import viewsets

from apps.reviews.models.review import Review
from apps.reviews.serializers import ReviewListSerializer, ReviewDetailSerializer, ReviewCreateSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ReviewListSerializer
        if self.action == "create":
            return ReviewCreateSerializer

        return ReviewDetailSerializer

    # Настроить права доступа

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
