from django.contrib import admin
from users.models import Contact, CustomUser


admin.site.register(Contact)
admin.site.register(CustomUser)