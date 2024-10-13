from django.contrib.auth.models import User
from django.db.models import BooleanField, CASCADE, CharField, DateTimeField, ForeignKey, ManyToManyField, Model

from pa_tag.models import Tag

class Note(Model):
    name = CharField(max_length=50, null=False)
    description = CharField(max_length=150, null=True)
    done = BooleanField(default=False)
    created = DateTimeField(auto_now_add=True)
    tags = ManyToManyField(Tag)

    user = ForeignKey(User, on_delete=CASCADE, related_name='note')

    def __str__(self):
        return self.name
