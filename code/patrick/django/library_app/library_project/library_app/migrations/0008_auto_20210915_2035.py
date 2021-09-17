# Generated by Django 3.2.7 on 2021-09-15 20:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library_app', '0007_rename_profile_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='checkout',
            old_name='user',
            new_name='profile',
        ),
    ]
