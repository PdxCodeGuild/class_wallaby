# Generated by Django 3.1.7 on 2021-02-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]