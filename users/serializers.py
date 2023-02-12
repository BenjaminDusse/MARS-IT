from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from users.models import Contact, CustomUser

class ContactSerializer(ModelSerializer):  

    class Meta:
        model = Contact
        fields = ['tg_user_id', 'chat_id', 'lang']

    # def save(self, **kwargs):
    #     # print(self.validated_data.get('tg_user_id'))
    #     # print(self.context.get('tg_user_id'))
    #     with transaction.atomic():
    #         tg_user_id = self.validated_data.get('tg_user_id')
    #         chat_id = self.validated_data.get('chat_id')
    #         lang = self.validated_data.get('lang')



    #         (contact, created) = Contact.objects.get_or_create(tg_user_id=self.context.get('tg_user_id'))

    #         CustomUser.objects.bulk_create(contact)
        # return super().save(**kwargs)

class CustomUserSerializer(ModelSerializer):
    contact = ContactSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'contact']

