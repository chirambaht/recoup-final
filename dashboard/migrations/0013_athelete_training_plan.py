# Generated by Django 3.0.8 on 2020-07-17 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_remove_athelete_training_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='athelete',
            name='training_plan',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.plan'),
        ),
    ]
