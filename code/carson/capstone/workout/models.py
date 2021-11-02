from django.db import models
from django.conf import settings
from django.urls import reverse


class Diary(models.Model):
    # date = models.DateField()
    meal = models.TextField()
    name = models.TextField()
    # amount = models.IntegerField()


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    
    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'