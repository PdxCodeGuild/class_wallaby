# Generated by Django 3.2.6 on 2021-09-14 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_complete',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]