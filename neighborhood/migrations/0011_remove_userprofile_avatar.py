# Generated by Django 4.0.5 on 2022-06-20 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0010_remove_location_geolocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
    ]