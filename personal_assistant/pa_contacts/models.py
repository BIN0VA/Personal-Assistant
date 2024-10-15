from django.contrib.auth.models import User
from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    EmailField,
    ForeignKey,
    Model,
    UniqueConstraint,
)


class Contact(Model):
    name = CharField(max_length=50, null=False)
    address = CharField(max_length=150, null=True)
    phone = CharField(max_length=20, null=False)
    email = EmailField(max_length=50, null=True, blank=True)
    birthday = DateField(null=True)

    user = ForeignKey(User, CASCADE, related_name='contacts')

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'phone'],
                name='unique_phone_per_user',
            ),
            UniqueConstraint(
                fields=['user', 'email'],
                name='unique_email_per_user',
            ),
        ]

    def save(self, *args, **kwargs):
        if self.email == '':
            self.email = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
