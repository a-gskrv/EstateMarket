from django.contrib import admin

from apps.listings.models import Listing, Location, Property, PropertyType

# Register your models here.

admin.site.register(Listing)
admin.site.register(Location)
admin.site.register(Property)
admin.site.register(PropertyType)
