# Generated by Django 3.2.8 on 2021-10-18 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_feeds'),
        ('info_app', '0004_alter_feeds_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='subscriber',
            field=models.ManyToManyField(null=True, to='users.Profile'),
        ),
    ]
