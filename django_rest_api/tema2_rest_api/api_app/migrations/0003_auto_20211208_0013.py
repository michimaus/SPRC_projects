# Generated by Django 3.2.9 on 2021-12-08 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_auto_20211207_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citymodel',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='countrymodel',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]