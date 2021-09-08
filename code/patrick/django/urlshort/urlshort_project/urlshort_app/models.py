from django.db import models

class Short(models.Model):
    code = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
