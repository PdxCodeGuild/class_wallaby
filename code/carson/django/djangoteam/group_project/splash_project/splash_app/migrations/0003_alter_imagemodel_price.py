# Generated by Django 3.2.7 on 2021-09-24 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash_app', '0002_imagemodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='price',
            field=models.IntegerField(),
        ),
    ]
