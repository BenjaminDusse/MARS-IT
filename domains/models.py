from django.db import models
from django.conf import settings
from general.models import BaseModel


class Domain(BaseModel):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='domain')


class UserPlan(BaseModel):
    title = models.CharField(max_length=200)
    is_recommended = models.BooleanField(default=False)
    price = models.CharField(max_length=15)
    discount = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

class UserPlanFeature(BaseModel):
    name = models.CharField(max_length=200)
    # user_plan = models.ForeignKey(UserPlan, on_delete=models.SET_NULL, null=True)
