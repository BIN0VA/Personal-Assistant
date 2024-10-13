from django.db.models import (
    BooleanField,
    CharField,
    FloatField,
    Model,
    TimeField,
    URLField,
)


class News(Model):
    title = CharField(max_length=200)
    link = URLField()
    time = TimeField()

    def __str__(self):
        return self.title


class Rate(Model):
    name = CharField(max_length=50)
    buy = FloatField()
    sell = FloatField()
    bank = BooleanField(default=False)

    def __str__(self):
        return self.name
