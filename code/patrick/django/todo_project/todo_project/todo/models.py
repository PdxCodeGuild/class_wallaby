from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    title = models.CharField(max_length=150)
    text_desc = models.CharField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now)
    
    completed = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title