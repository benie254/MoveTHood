# Generated by Django 4.0.5 on 2022-06-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0007_alter_location_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(default='Nairobi', max_length=255),
        ),
    ]