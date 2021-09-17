from django.db import models
from django.contrib.auth.models import User
import shutil

class ImageModel(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    thumb = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='pics')
    photographer = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    alt_description = models.CharField(max_length=200, blank=True, null=True)
    raw = models.CharField(max_length=200)
    full = models.CharField(max_length=200)
    small = models.CharField(max_length=200)
    regular = models.CharField(max_length=200)
    download = models.CharField(max_length=200)
    id = models.CharField(max_length=200, primary_key=True)
    width = models.CharField(max_length=200)
    height = models.CharField(max_length=200)

    def __str__(self):
        return self.id


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)