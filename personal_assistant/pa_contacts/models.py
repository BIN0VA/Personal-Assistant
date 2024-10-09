from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=12, unique=True, null=False)
    email = models.CharField(max_length=50, null=True, blank=True)
    birthday = models.DateField(null=True)

    def __str__(self):
        return self.name
