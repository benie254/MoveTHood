# Generated by Django 4.0.5 on 2022-06-20 09:12

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0006_alter_business_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='address',
            field=location_field.models.plain.PlainLocationField(max_length=63),
        ),
    ]
