from django.db import models
from django.db.models.functions import Lower


class ContactType(models.Model):
    name = models.CharField(
        max_length=30,
        # unique=True
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