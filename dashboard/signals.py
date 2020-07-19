
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Athelete,plan


@receiver(post_save, sender=User)
def create_athelete(sender, instance, created, **kwargs):
    if created:
        t_p = plan.objects.create(type="Training")
        Athelete.objects.create(athelete=instance, training_plan=t_p, paid = False, trainer=False, practice=False)


@receiver(post_save, sender=User)
def save_athelete(sender, instance,*args, **kwargs):
    instance.athelete.save()