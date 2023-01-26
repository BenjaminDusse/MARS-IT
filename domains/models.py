from django.db import models
from django_extensions.db.models import TimeStampedModel
from core.models import CustomUser
from django.conf import settings

UZ = "uz"
RU = "ru"


PHONE = "phone"
TELEGRAM = "telegram"
BOTH = "both"

class Contact(TimeStampedModel):

    LANGUAGE_CHOICE = (
        (UZ, 'uz'),
        (RU, 'ru'),
    )
    CONTACT_TYPE = (
        (PHONE, 'phone'),
        (TELEGRAM, 'telegram'),
        (BOTH, 'both'),
    )

    tg_user_id = models.PositiveBigIntegerField(unique=True, null=True)
    chat_id = models.PositiveBigIntegerField(unique=True, null=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    lang = models.CharField(max_length=3, choices=LANGUAGE_CHOICE, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    code = models.CharField(max_length=12, null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.user.get_username()