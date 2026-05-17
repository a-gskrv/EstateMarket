from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)
from rest_framework.routers import DefaultRouter


from apps.analytics.views import AnalyticsView
from apps.bookings.views.booking import BookingViewSet
from apps.listings.views import (
    ListingViewSet,
    PropertyViewSet,
    PropertyTypeViewSet)
from apps.reviews.views import ReviewViewSet
from apps.users.views import LoginUser, LogoutUser, RegisterUserView, RefreshUserTokenView

router = DefaultRouter()
router.register("bookings", BookingViewSet, basename="booking")

router.register("listings", ListingViewSet, basename="listing")
router.register("properties", PropertyViewSet, basename="property")
router.register("property_types", PropertyTypeViewSet, basename="property_type")

router.register("reviews", ReviewViewSet, basename="review")

urlpatterns = [
    path("", include(router.urls)),
    path("analytics/", AnalyticsView.as_view(), name="analytics"),

    # path('jwt-login/', TokenObtainPairView.as_view()),

    path("auth/login/", LoginUser.as_view(), name="login"),
    path("auth/refresh-token/", RefreshUserTokenView.as_view(), name='refresh_token'),
    path("auth/logout/", LogoutUser.as_view(), name="logout"),
    path("auth/register/", RegisterUserView.as_view(), name="register"),
]
