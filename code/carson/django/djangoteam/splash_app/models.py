from django.db import models

# from django.contrib.auth.models import User
# import shutil

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


# class ProfileModel(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # products = models.ManyToManyField('Product', blank=True)
#     id = models.CharField(max_length=200, primary_key=True)

#     def __str__(self):
#         return f'{self.user.username}'

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import ProfileModel

  
  
# @receiver(post_save, sender=User) 
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         ProfileModel.objects.create(user=instance)


# class Item(models.Model):
#     image = models.OneToOneField('ImageModel', on_delete=models.SET_NULL, null=True, blank=True)
#     is_ordered = models.BooleanField(default=False)
#     date_ordered = models.DateTimeField(null=True)
    
#     def __str__(self):
#         return self.image.id 

# class Order(models.Model):
#     ref_num = models.CharField(max_length=20)
#     profile = models.ForeignKey('ProfileModel', on_delete=models.SET_NULL, null=True)
#     is_ordered = models.BooleanField(default=False)
#     items = models.ManyToManyField(Item)
#     date_ordered = models.DateTimeField(null=True)

#     def get_cart_items(self):
#         return self.items.all()

#     def get_cart_total(self):
#         return sum([item.image.price for item in self.items.all()])
    
#     def __str__(self):
#         return self.ref_num



# def profile_create(sender, instance, )