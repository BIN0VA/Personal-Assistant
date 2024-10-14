from cloudinary.models import CloudinaryField
from django.db.models import CASCADE, CharField, DateTimeField, ForeignKey, \
    Model
from django.contrib.auth.models import User


class File(Model):
    CATEGORIES = (
        ('image', 'Image'),
        ('text', 'Document'),
        ('music', 'Audio'),
        ('play', 'Video'),
        ('zip', 'Archive'),
        ('code', 'Code'),
        ('unknown', 'Unknown'),
    )

    file = CloudinaryField('file')
    uploaded_at = DateTimeField(auto_now_add=True)
    category = CharField(max_length=10, choices=CATEGORIES)

    # Прив'язка до користувача
    user = ForeignKey(User, CASCADE)

    def __str__(self):
        return f'{self.file.url.split("/")[-1]} ({self.user.username})'
