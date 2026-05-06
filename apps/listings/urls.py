from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.listings.views import (
    ListingViewSet,
    PropertyViewSet,
    PropertyTypeViewSet)

router = DefaultRouter()
router.register("listings", ListingViewSet, basename="listing")
router.register("properties", PropertyViewSet, basename="property")
router.register("property_types", PropertyTypeViewSet, basename="property_type")

urlpatterns = [
    path("", include(router.urls)),
]
