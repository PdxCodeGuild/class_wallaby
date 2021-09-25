from django.db import models

class GetImages(models.Model):
    full = models.CharField(max_length = 500,  blank = True,)
    thumb = models.CharField(max_length = 500,  blank = True,)
    download = models.CharField(max_length = 500,  blank = True)
    my_image = models.ImageField(upload_to ='images/')

class Board(models.Model):
    full = models.CharField(max_length = 500, blank = True,)
    thumb = models.CharField(max_length = 500, blank = True,)
    download = models.CharField(max_length = 500,  blank = True)
