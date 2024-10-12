from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class PaUploadedFile(models.Model):
    CATEGORY_CHOICES = [
        ('image', 'Image'),
        ('document', 'Document'),
        ('video', 'Video'),
        ('other', 'Other')
    ]
    file = CloudinaryField('file')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Прив'язка до користувача

    def __str__(self):
        return f'{self.file.url.split("/")[-1]} ({self.user.username})'
