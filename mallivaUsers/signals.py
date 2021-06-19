from django.dispatch import Signal, receiver
from django.db.models.signals import pre_save
from .models import User


@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
    """
    set username from submited email
    """

    if instance.username is None:
        instance.username = instance.email.split("@")[0]
    else:
        pass
