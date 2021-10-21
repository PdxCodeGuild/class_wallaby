# Generated by Django 3.2.8 on 2021-10-15 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_feeds'),
        ('info_app', '0002_alter_feeds_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='subscriber',
            field=models.ManyToManyField(related_name='related_id', to='users.Profile'),
        ),
    ]
