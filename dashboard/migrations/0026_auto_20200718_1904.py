# Generated by Django 3.0.8 on 2020-07-18 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_auto_20200718_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kb',
            old_name='injury',
            new_name='Focus_Area',
        ),
    ]
