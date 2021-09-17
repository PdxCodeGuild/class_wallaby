from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User
import uuid

class Book(models.Model):
    
    title = models.CharField(max_length=200)
    publish_date = DateTimeField()
    author = models.ForeignKey('author', on_delete=models.CASCADE) #should be many to many

    class Meta:
        ordering = ["title"]
    
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Checkout(models.Model):
    
    profile = models.ForeignKey('Profile', on_delete=models.RESTRICT, null=True)
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    checked_out = models.DateField(null=True, blank=True)
    due_back = models.DateField(null=True, blank=True)
    
    LOAN_STATUS = (
    ('m', 'Maintenance'),
    ('o', 'On loan'),
    ('a', 'Available'),
    ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
        
    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.book}'
