from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name - models.CharField(max_length=30)
    email = models.EmailField()

    def__str__(self):
        return self.first_name

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    pub_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title