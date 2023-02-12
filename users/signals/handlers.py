from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Contact, CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=Contact)
def create_user_for_new_contact(sender, **kwargs):
    print(kwargs)
    if kwargs['created']:
        user = User.objects.create()
        CustomUser.objects.create(user=kwargs['instance'])

