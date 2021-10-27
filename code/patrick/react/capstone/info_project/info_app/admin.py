from django.contrib import admin
from .models import Feeds, UserSubscriptions, FeedName
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

admin.site.register(Feeds)
admin.site.register(UserSubscriptions)
admin.site.register(FeedName)