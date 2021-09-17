# Generated by Django 3.2.7 on 2021-09-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort_app', '0003_short_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='short',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='short',
            name='slug',
        ),
        migrations.AlterField(
            model_name='short',
            name='code',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
