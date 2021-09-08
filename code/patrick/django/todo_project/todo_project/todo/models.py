from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Todo(models.Model):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    complete = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']