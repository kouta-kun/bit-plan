# Generated by Django 2.2.5 on 2019-09-16 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.TextField(default=''),
        ),
    ]
