from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from general.utils.choices import Languages
from general.models import BaseModel
from django.contrib.auth import get_user_model

class Contact(BaseModel):
    chat_id = models.PositiveBigIntegerField(unique=True, null=True)
    lang = models.CharField(max_length=3, choices=Languages.choices, default=Languages.UZ)

class CustomUser(AbstractUser):
    user_plan = models.ForeignKey('UserPlan', on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    contact = models.OneToOneField(Contact, on_delete=models.PROTECT, related_name='user', null=True, blank=True)

class UserPlan(BaseModel):
    title = models.CharField(max_length=200)
    is_recommended = models.BooleanField(default=False)
    price = models.CharField(max_length=15)
    discount = models.PositiveSmallIntegerField(default=0)


    def __str__(self):
        return self.title

class UserPlanFeature(BaseModel):
    name = models.CharField(max_length=200)
    user_plan = models.ForeignKey(UserPlan, on_delete=models.SET_NULL, null=True, blank=True)


