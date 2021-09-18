# Generated by Django 3.2.7 on 2021-09-17 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('splash_app', '0005_rename_profile_profilemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_ordered', models.DateTimeField(null=True)),
                ('image', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='splash_app.imagemodel')),
            ],
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_num', models.CharField(max_length=20)),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_ordered', models.DateTimeField(null=True)),
                ('items', models.ManyToManyField(to='splash_app.Item')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='splash_app.profilemodel')),
            ],
        ),
    ]
