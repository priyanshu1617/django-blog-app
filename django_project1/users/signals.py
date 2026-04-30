from django.db.models.signals import post_save
#signal will get fired when an object is created
from django.contrib.auth.models import User 
#User model is the sender who will send the signal
from django.dispatch import receiver
#receiver is function who receives the signal
from .models import Profile 

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.created(user=instance)

def save_profile(sender, instance, **kwargs):
    instance.profile.save()

