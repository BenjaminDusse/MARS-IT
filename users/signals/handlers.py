from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from domains.models import Contact

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_for_new_contact(sender, **kwargs):
    if kwargs["created"]:
        Contact.objects.create(user=kwargs["instance"])
