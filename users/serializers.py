from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from users.models import Contact, CustomUser, UserPlan, UserPlanFeature

class ContactCreateSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = ['chat_id', 'lang']

class ContactSerializer(ModelSerializer):
    
    class Meta:
        model = Contact
        fields = ['chat_id', 'lang']


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

class UserPlanFeature(ModelSerializer):
    
    class Meta:
        model = UserPlanFeature
        fields = ['name', 'user_plan']


class UserPlanSerializer(ModelSerializer):
    features = UserPlanFeature(many=True, read_only=True)
    
    class Meta:
        model = UserPlan
        fields = ['id', 'title', 'price', 'discount', 'is_recommended', 'features']


class CustomUserSerializer(ModelSerializer):
    user_plan = UserPlanSerializer
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'user_plan']

    def create(self, validated_data):
        chat_id = self.context['request'].chat_id
    
        try:
            Contact.objects.create(chat_id=chat_id)
        except Exception as e:
            print(f"Error occurs: { e }")
        return super().create(validated_data)


