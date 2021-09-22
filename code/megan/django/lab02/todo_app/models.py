from datetime import datetime
from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    # date_entered = models.DateField(datetime)
    # date_completed = models.DateField(datetime) 

    TODO_TYPE = (
        ('p', 'personal'),
        ('s', 'school'),
        ('w', 'work'),
        ('f', 'family'),
        ('m', 'misc'),
    )

    todo_type = models.CharField(max_length=1, choices=TODO_TYPE, blank=True, default='m')

    # todo_date = models.DateField(timezone.now())

    def __str__(self):
        return self.title