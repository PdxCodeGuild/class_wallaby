from django.db import models
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return "%s" % (self.user)

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # image = models.ImageField(upload_to ='images/')
    price = models.PositiveIntegerField(default=0, null=False, blank=False)
    quantity = models.PositiveIntegerField(default=1, null=False,  blank=False )
    session = models.ForeignKey(Cart, null=True, blank=True, on_delete=PROTECT)



    
    def __str__(self):
        return "%s %s" % (self.title, self.session)


