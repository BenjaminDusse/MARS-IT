from django.contrib import admin
from users.models import Contact, CustomUser, UserPlan, UserPlanFeature

admin.site.register(Contact)
admin.site.register(CustomUser)
admin.site.register(UserPlan)
admin.site.register(UserPlanFeature)
