from django.db import models
from django.db.models.functions import Lower


class ContactInfo(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="contacts",
    )

    contact_type = models.ForeignKey(
        "users.ContactType",
        on_delete=models.CASCADE
    )

    value = models.CharField(max_length=255)

    is_public = models.BooleanField(default=False)

    def __str__(self):
        str_contact_info = f"{self.contact_type.name}: {self.value}"
        return str_contact_info

    class Meta:
        db_table = 'users_contact_info'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'contact_type'],
                name='unique_user_contact_type'
            )
        ]


class ContactType(models.Model):
    name = models.CharField(
        max_length=30,
    )

    add_by_default = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users_contact_type'
        verbose_name = 'Contact Type'
        verbose_name_plural = 'Contact Types'

        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='unique_name_users_contact_type'
            )
        ]
