# Generated by Django 3.2.7 on 2021-09-15 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0005_checkout_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='profile',
            new_name='user',
        ),
    ]
