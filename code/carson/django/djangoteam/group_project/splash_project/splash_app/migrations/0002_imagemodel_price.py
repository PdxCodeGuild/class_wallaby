# Generated by Django 3.2.7 on 2021-09-22 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='price',
            field=models.IntegerField(default=5, max_length=10),
            preserve_default=False,
        ),
    ]
