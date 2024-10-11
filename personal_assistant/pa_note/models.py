from django.db.models import BooleanField, CharField, DateTimeField, Model


class Note(Model):
    name = CharField(max_length=50, null=False)
    description = CharField(max_length=150, null=True)
    done = BooleanField(default=False)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
