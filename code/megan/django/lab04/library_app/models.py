from django.db import models
from django.db.models.fields import CharField, DateField
from django.db.models.fields.related import ForeignKey

#  Author: a model representing an author of a book, one author can have multiple books
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.last_name

# Book: a model representing a book, with a title, publish date, and an author (foreign key)
class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.title