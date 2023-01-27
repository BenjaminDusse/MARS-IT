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

    phone_number = models.CharField(max_length=25, null=True, blank=True)
    lang = models.CharField(max_length=3, choices=LANGUAGE_CHOICE, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    code = models.CharField(max_length=12, null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')



    def __str__(self):
        return self.user.get_username()


class Domain(TimeStampedModel):
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='domain')
    
    

class ContactPlan(TimeStampedModel):
    title = models.CharField(max_length=200)
    is_recommended = models.BooleanField(default=False)
    price = models.CharField(max_length=15)
    discount = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title
    
class ContactPlanFeature(TimeStampedModel):
    name = models.CharField(max_length=200)


class PaymentHistory(TimeStampedModel):
    pass

