# Generated by Django 3.2.8 on 2021-11-01 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedName',
            fields=[
                ('feed_name', models.CharField(max_length=500, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSubscriptions',
            fields=[
                ('user_id', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('AvailableFeeds', models.ManyToManyField(blank=True, to='info_app.FeedName')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, unique=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('pubDate', models.DateField(null=True)),
                ('link', models.CharField(max_length=500)),
                ('feed', models.CharField(max_length=500)),
                ('subscriber', models.ManyToManyField(blank=True, to='users.Profile')),
            ],
        ),
    ]
