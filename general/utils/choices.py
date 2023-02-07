from django.db import models

class Languages(models.TextChoices):
    UZ = 'UZ', ('Uzbek')
    RU = 'RU', ('Russian')
