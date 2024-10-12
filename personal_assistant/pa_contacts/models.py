from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=20, unique=True, null=False)
    email = models.EmailField(max_length=50, unique=True, null=True, blank=True)
    birthday = models.DateField(null=True)

    def save(self, *args, **kwargs):
        if self.email == '':
            self.email = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
