# Generated by Django 2.2.4 on 2019-08-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videonews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='editor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]