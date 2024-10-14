from django.contrib.auth.models import User
from django.db.models import CASCADE, CharField, ForeignKey, Model


class Tag(Model):
    name = CharField(max_length=50, unique=True)
    user = ForeignKey(User, CASCADE, 'tag')

    def __str__(self):
        return self.name
