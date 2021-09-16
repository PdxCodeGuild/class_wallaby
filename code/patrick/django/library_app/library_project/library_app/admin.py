from django.contrib import admin
from .models import Book, Author, Profile, Checkout

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(Checkout)