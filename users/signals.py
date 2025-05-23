from .models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail
import os

# The dispatch_uid is a unique identifier used to prevent a signal from being connected more than once.
@receiver(post_save, sender=CustomUser, dispatch_uid="send_welcome_email")
def send_welcome_email(sender, instance, created, **kwargs):
    """Send a welcome email when a new user is created"""
    print("Signal fired...")
    if created:
        send_mail(
            "Welcome!",
            "Thanks for signing up!",
            "admin@django.com",
            [instance.email],
            fail_silently=False,
        )


@receiver(post_delete, sender=CustomUser)
def delete_associated_file(sender, instance, **kwargs):
    """Delete the file from the filesystem if it exists."""
    if instance.cv:
        if os.path.isfile(instance.cv.path):
            os.remove(instance.cv.path)


            
            