from django.db import models

class ImageModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics')
    photographer = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    raw = models.CharField(max_length=200)
    full = models.CharField(max_length=200)
    small = models.CharField(max_length=200)
    regular = models.CharField(max_length=200)
    download = models.CharField(max_length=200)