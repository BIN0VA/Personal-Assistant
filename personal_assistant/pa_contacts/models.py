from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, null=True, blank=True)
    birthday = models.DateField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'phone'], name='unique_phone_per_user'),
            models.UniqueConstraint(fields=['user', 'email'], name='unique_email_per_user')
        ]

    def save(self, *args, **kwargs):
        if self.email == '':
            self.email = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
