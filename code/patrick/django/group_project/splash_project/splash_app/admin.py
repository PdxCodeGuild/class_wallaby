from django.contrib import admin
from .models import ImageModel, ProfileModel, Item, Order

admin.site.register(ImageModel)
admin.site.register(ProfileModel)
admin.site.register(Item)
admin.site.register(Order)
