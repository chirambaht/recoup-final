# Generated by Django 3.0.8 on 2020-07-16 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0003_auto_20200716_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='athelete',
            name='profile_pic',
            field=models.ImageField(default='new_face.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='athelete',
            name='athelete',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='practice',
            name='practice',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Trainer',
        ),
    ]
