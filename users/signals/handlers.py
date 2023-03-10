from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from users.models import Contact, CustomUser

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_for_new_user(sender, instance: Contact,  **kwargs):
    if kwargs['created']:
        Contact.objects.create()
        

