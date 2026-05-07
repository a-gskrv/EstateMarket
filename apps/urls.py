from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.bookings.views.booking import BookingViewSet
from apps.listings.views import (
    ListingViewSet,
    PropertyViewSet,
    PropertyTypeViewSet)
from apps.reviews.views import ReviewViewSet

router = DefaultRouter()
router.register("bookings", BookingViewSet, basename="booking")

router.register("listings", ListingViewSet, basename="listing")
router.register("properties", PropertyViewSet, basename="property")
router.register("property_types", PropertyTypeViewSet, basename="property_type")


router.register("reviews", ReviewViewSet, basename="review")

urlpatterns = [
    path("", include(router.urls)),
]
