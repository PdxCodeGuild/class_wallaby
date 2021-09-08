from django.db import models
from django.urls import reverse
class Short(models.Model):
    code = models.CharField(max_length=200)
    url = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse('short-detail', kwargs={'pk': self.pk})




