# Generated by Django 3.2 on 2022-06-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='intro',
            field=models.TextField(default='Intro', max_length=80),
        ),
    ]
