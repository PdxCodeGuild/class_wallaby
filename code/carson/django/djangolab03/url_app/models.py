from django.db import models

class URL_shorten(models.Model):
    original = models.CharField(max_length=500)
    updated = models.CharField(max_length=500)
    def __str__(self):
        return self.original