from django.db import models
from django.conf import settings
from general.models import BaseModel

class Domain(BaseModel):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='domain')

# register
# telegram botdan api ga request jonatib userni create
# get method func yozish
# har kuni userni domainini vaqtini check qilib turish kerak.
# celery da worker ni alohida run qilinadi
# crontab ishlatish kere
