from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title
