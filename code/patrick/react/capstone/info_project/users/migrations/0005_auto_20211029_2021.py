# Generated by Django 3.2.8 on 2021-10-30 03:21

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image_ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(default='default.jpg', height_field='height', upload_to='profile_pics', verbose_name='Image', width_field='width'),
        ),
    ]
