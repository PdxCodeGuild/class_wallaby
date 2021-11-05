from django.db import models

class Gestures(models.Model):
  name = models.CharField(max_length=50)
  timesCorrect = models.SmallIntegerField(default=0)
  timesIncorrect = models.SmallIntegerField(default=0)
  dateCorrect = models.DateTimeField(auto_now=True)
  imgURL = models.CharField(max_length=500)
  bin = models.SmallIntegerField(default=0)