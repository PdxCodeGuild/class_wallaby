# Generated by Django 3.2.8 on 2021-10-12 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_feeds'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='feeds',
        ),
    ]
