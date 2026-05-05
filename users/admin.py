from django.contrib import admin

from users.models import User, ContactInfo, ContactType

# Register your models here.

admin.site.register(User)
admin.site.register(ContactInfo)
admin.site.register(ContactType)