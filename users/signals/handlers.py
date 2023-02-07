from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Contact, CustomUser

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_contact_for_new_user(sender, **kwargs):
    if kwargs["created"]:
        Contact.objects.create(user=kwargs["instance"])
