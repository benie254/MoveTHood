# Generated by Django 4.0.5 on 2022-06-21 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0015_alter_business_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='address',
        ),
    ]
