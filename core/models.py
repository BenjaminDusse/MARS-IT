from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    tg_user_id = models.PositiveBigIntegerField(unique=True, null=True)
    chat_id = models.PositiveBigIntegerField(unique=True, null=True)

    def get_username(self):
        return self.username

