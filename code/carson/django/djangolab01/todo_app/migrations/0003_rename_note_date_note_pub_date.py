# Generated by Django 3.2.7 on 2021-09-03 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_rename_user_note_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='note_date',
            new_name='pub_date',
        ),
    ]
