# Generated by Django 3.2.7 on 2021-10-14 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0004_auto_20211014_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetup',
            name='location',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
