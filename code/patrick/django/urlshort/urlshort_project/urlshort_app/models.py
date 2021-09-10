from django.db import models
from django.db.models.fields import DateTimeField
from django.urls import reverse
class Short(models.Model):
    code = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    date = DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=10, unique=True, blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f'{self.url} to {self.code}'
    
    def get_absolute_url(self):
        return reverse('short-detail', kwargs={'pk': self.pk})




