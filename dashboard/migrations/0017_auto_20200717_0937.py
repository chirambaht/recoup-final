# Generated by Django 3.0.8 on 2020-07-17 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20200717_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='type',
            field=models.CharField(choices=[('Recovery', 'Recovery'), ('Training', 'Training')], default='Training', max_length=10, null=True),
        ),
    ]
