from django.db import models
from django.db.models.deletion import PROTECT

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='images/')
    price = models.PositiveIntegerField(default=0, null=False, blank=False)
    quantity = models.PositiveIntegerField(default=1, null=False,  blank=False )

    
    def __str__(self):
        return "%s %s" % (self.title, self.price)


class Cart(models.Model):
    session = models.ForeignKey(Product, null=True, blank=True, on_delete=PROTECT)

