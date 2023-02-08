from rest_framework import viewsets

from users.serializers import ContactSerializer, CustomUserSerializer
from users.models import CustomUser, Contact


class ContactViewSet(viewsets.ModelViewSet):
    
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    

class CustomUserViewSet(viewsets.ModelViewSet):
    
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
