# Generated by Django 3.1.4 on 2020-12-30 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0007_auto_20201230_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='available_authors',
            field=models.CharField(blank=True, choices=[('e.h', 'ERNEST HEMINGWAY'), ('j.d', 'JOAN DIDION'), ('r.b', 'RAY BRADBURY'), ('a.r', 'AYN RAND'), ('g.f', 'GILLIAN FLYNN'), ('j.a', 'JANE AUSTEN')], default='ERNEST', max_length=200),
        ),
    ]
