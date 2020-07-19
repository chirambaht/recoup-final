from django.db import models
from jsonfield import JSONField
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Practice(models.Model):
    practice = models.CharField(max_length=100)
    owner = models.CharField(max_length=50)
    practiceNumber = models.CharField(max_length=10)
    address = models.TextField()
    contact_number = models.CharField(max_length=10)
    contact_email = models.EmailField()

    def __str__(self):
        return self.practice


class plan(models.Model):
    Monday_Title =   models.CharField(max_length=20, null=True)
    Monday_Description = models.TextField(null=True)
    Tuesday_Title =   models.CharField(max_length=20, null=True)
    Tuesday_Description = models.TextField(null=True)
    Wednesday_Title =   models.CharField(max_length=20, null=True)
    Wednesday_Description = models.TextField(null=True)
    Thursday_Title =   models.CharField(max_length=20, null=True)
    Thursday_Description = models.TextField(null=True)
    Friday_Title =   models.CharField(max_length=20, null=True)
    Friday_Description = models.TextField(null=True)
    Saturday_Title =   models.CharField(max_length=20, null=True)
    Saturday_Description = models.TextField(null=True)
    Sunday_Title =   models.CharField(max_length=20, null=True)
    Sunday_Description = models.TextField(null=True)
    Sunday_Video_url = models.CharField(max_length=60, null=True, default='ScMzIvxBSi4')
    Monday_Video_url = models.CharField(max_length=60, null=True, default='ScMzIvxBSi4')
    Tuesday_Video_url = models.CharField(max_length=60, null=True, default='ScMzIvxBSi4')
    Wednesday_Video_url = models.CharField(max_length=60, null=True, default='ScMzIvxBSi4')
    Thursday_Video_url = models.CharField(max_length=60, null=True, default='ScMzIvxBSi4')
    Friday_Video_url = models.CharField(max_length=60, null=True, default='ScMzIvxBSi4')
    Saturday_Video_url = models.CharField(max_length=60, null=True, default='ScMzIvxBSi4')
    
    type = models.CharField(max_length=10, choices=[('Recovery','Recovery'), ('Training', 'Training')], default='Training', null=True)
    
    def __str__(self):
        return self.type

class Athelete(models.Model):
    athelete = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='new_face.jpg', upload_to='profile_pics')
    training_plan = models.OneToOneField(plan, on_delete=models.PROTECT,null=True)
    contact_number = models.CharField(max_length=10)
    contact_email = models.EmailField()
    SPORTS = [
        ('CYC','Road Cycling'),
        ('MTB','Mountain Biking'),
        ('TRR','Trail Running'),
        ('RDR','Road Running'),
        ('SWM','Swimming'),
        ('PLT','Pilates'),
        ('STR','Stretching'),
    ]
    sport = models.CharField(
        choices=SPORTS,
        default='Stretching',
        max_length=16
    )
    trainer = models.BooleanField()
    practice = models.BooleanField()
    paid = models.BooleanField()
    
    def __str__(self):
        return self.athelete.username

    def save(self, *args, **kwargs):
        super(Athelete, self).save(*args, **kwargs)

        try:
            img = Image.open(self.profile_pic.path)

            new_img = img.resize((500,500))
            new_img.save(self.profile_pic.path)
        except:
            pass

class KB(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    practice = models.CharField(max_length=30)
    presenter = models.CharField(max_length=50)
    Focus_Area = models.TextField()
    thumbnail = models.ImageField(default='thumbs.jpg', upload_to='thumbnails')
    url = models.CharField(max_length=60)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(KB, self).save(*args, **kwargs)

        img = Image.open(self.thumbnail.path)

        new_img = img.resize((192,108))
        new_img.save(self.thumbnail.path)
