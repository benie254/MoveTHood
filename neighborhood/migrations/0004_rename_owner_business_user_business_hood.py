# Generated by Django 4.0.5 on 2022-06-20 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0003_remove_policedept_chief_chama_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='owner',
            new_name='user',
        ),
        migrations.AddField(
            model_name='business',
            name='hood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='neighborhood.userhood'),
        ),
    ]