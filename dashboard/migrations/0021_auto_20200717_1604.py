# Generated by Django 3.0.8 on 2020-07-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_auto_20200717_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='Friday_Video_url',
            field=models.CharField(default='ScMzIvxBSi4', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='Monday_Video_url',
            field=models.CharField(default='ScMzIvxBSi4', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='Saturday_Video_url',
            field=models.CharField(default='ScMzIvxBSi4', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='Sunday_Video_url',
            field=models.CharField(default='ScMzIvxBSi4', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='Thursday_Video_url',
            field=models.CharField(default='ScMzIvxBSi4', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='Tuesday_Video_url',
            field=models.CharField(default='ScMzIvxBSi4', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='Wednesday_Video_url',
            field=models.CharField(default='ScMzIvxBSi4', max_length=60, null=True),
        ),
    ]
