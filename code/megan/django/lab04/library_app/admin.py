from django.contrib import admin

from . import models

admin.site.register(models.Author)
admin.stie.register(models.Book)