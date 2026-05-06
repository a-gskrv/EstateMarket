import django_filters

from .models import Listing


class ListingFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte'
    )

    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte'
    )

    min_rooms_count = django_filters.NumberFilter(
        field_name='property__rooms_count',
        lookup_expr='gte'
    )

    max_rooms_count = django_filters.NumberFilter(
        field_name='property__rooms_count',
        lookup_expr='lte'
    )

    class Meta:
        model = Listing
        fields = [
            'min_price',
            'max_price',
            'property__location__region',
            'property__location__city',
            'min_rooms_count',
            'max_rooms_count',
            'property__property_type',
        ]
