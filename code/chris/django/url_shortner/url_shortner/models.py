from django.db import models

# Create your models here.
class Url(models.Model):
  lurl = models.CharField(max_length=999)
  surl = models.CharField(max_length=30)
  def __str__(self):
    return self.lurl
