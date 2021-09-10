from django.db import models
from django.db.models.fields import DateTimeField
from django.urls import reverse
from .code_gen import create_random_code
class Short(models.Model):
    url = models.CharField(max_length=300)
    date = DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=10, unique=True, blank=True, primary_key=True)

    objects = models.Manager()
    class Meta:
        ordering = ["-date"]

    # def __str__(self):
    #     return f'{self.url} to {self.code}'
    
    def get_absolute_url(self):
        return reverse('short-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.code:
            # We pass the model instance that is being saved
            self.code = create_random_code(self)

        super().save(*args, **kwargs)



