# Generated by Django 3.2.7 on 2021-09-07 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-complete']},
        ),
    ]
