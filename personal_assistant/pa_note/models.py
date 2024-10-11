from django.db import models

class Note(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150, null=True)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
