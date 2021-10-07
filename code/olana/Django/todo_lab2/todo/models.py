from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    content = models.TextField()
    title = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
