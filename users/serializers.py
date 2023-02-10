from rest_framework.serializers import ModelSerializer
from users.models import Contact, CustomUser

class ContactSerializer(ModelSerializer):
    
    class Meta:
        model = Contact
        fields = ['user_plan', 'phone_number']
        


class CustomUserSerializer(ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'password', 'lang']

class CustomUserDetailSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['tg_user_id']
    
