from django.db import models
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return "%s" % (self.user)

class Product(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)
    session = models.ForeignKey(Cart, null=True, blank=True, on_delete=PROTECT)



    
    def __str__(self):
        return "%s %s" % (self.title, self.session)


