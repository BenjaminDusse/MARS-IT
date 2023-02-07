from django.db import models
from general.models import BaseModel
from django.conf import settings

# Create your models here.
class PaymentHistory(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='payment_history')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
