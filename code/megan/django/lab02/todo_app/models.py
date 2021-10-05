from django.db import models

class Todo(models.Model):
    text = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    date_completed = models.DateTimeField(null=True) 

    def __str__(self):
        return self.text