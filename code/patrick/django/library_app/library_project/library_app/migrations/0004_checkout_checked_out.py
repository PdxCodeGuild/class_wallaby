# Generated by Django 3.2.7 on 2021-09-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='checked_out',
            field=models.DateField(blank=True, null=True),
        ),
    ]