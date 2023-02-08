from rest_framework.serializers import ModelSerializer
from users.models import Contact, CustomUser

class ContactSerializer(ModelSerializer):
    
    class Meta:
        model = Contact
        fields = ['tg_user_id', 'chat_id', 'lang', 'user_plan', 'phone_number', 'user']
        

class CustomUserSerializer(ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'password']
