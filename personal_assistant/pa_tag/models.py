from django.contrib.auth.models import User
from django.db.models import CharField, ForeignKey, Model, SET_NULL


class Tag(Model):
    name = CharField(max_length=50, unique=True)
    user = ForeignKey(User, SET_NULL, 'tag', null=True, blank=True)

    def __str__(self):
        return self.name
