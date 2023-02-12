from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from users.models import Contact, CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=Contact)
def create_customer_for_new_user(sender, instance: Contact,  **kwargs):
    if kwargs['created']:
        # Contact.objects.create(user=kwargs['instance'])
        user = CustomUser.objects.create(username=str(instance.tg_user_id))
        instance.user = user
        instance.save()
