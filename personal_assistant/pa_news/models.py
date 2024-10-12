from django.db.models import CharField, DateTimeField, Model, TextField, \
    URLField


class News(Model):
    title = CharField(max_length=255)
    description = TextField()
    url = URLField()
    published_at = DateTimeField()

    def __str__(self):
        return self.title
