# Generated by Django 3.2.7 on 2021-09-15 20:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library_app', '0006_rename_profile_checkout_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='User',
        ),
    ]
