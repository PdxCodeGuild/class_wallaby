from django.contrib import admin
from .models import Feeds, UserSubscriptions, FeedName




admin.site.register(Feeds)
admin.site.register(UserSubscriptions)
admin.site.register(FeedName)