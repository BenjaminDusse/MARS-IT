from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from general.utils.choices import Languages
from general.models import BaseModel
from django.contrib.auth import get_user_model


class Contact(BaseModel):
    user_plan = models.OneToOneField('domains.UserPlan', on_delete=models.CASCADE, related_name='user_plan', null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class CustomUser(AbstractUser):
    tg_user_id = models.PositiveBigIntegerField(unique=True, null=True, blank=True)
    chat_id = models.PositiveBigIntegerField(unique=True, null=True, blank=True)
    lang = models.CharField(max_length=3, choices=Languages.choices, default=Languages.UZ)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='contact', null=True, blank=True)

