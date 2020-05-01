# this signal gets fired after an object is saved.
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# a receiver is a function that receives signals and then performs some tasks
from django.dispatch import receiver
from .models import Profile


# when a user is saved, send the signal post_save and that signal is going to be received by the receiver
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # this function runs everytime a user is created
    if created:
        # if a profile is created, then create a user object with the instance of the user that was created
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
