from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from general.utils.choices import Languages
from general.models import BaseModel
from django.contrib.auth import get_user_model
from domains.models import UserPlan

class Contact(BaseModel):
    tg_user_id = models.PositiveBigIntegerField(unique=True, null=True, blank=True)
    chat_id = models.PositiveBigIntegerField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    lang = models.CharField(max_length=3, choices=Languages.choices, default=Languages.UZ)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user', blank=True, null=True)

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"

class CustomUser(AbstractUser):
    first_name = None
    last_name = None


    user_plan = models.OneToOneField(UserPlan, on_delete=models.CASCADE, related_name='user_plan', null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    

    # def __str__(self):
    #     return self.contact