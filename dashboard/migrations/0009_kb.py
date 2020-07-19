# Generated by Django 3.0.8 on 2020-07-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20200716_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='KB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('practice', models.CharField(max_length=30)),
                ('presenter', models.CharField(max_length=50)),
                ('injury', models.TextField()),
                ('url', models.CharField(max_length=60)),
            ],
        ),
    ]
