from rest_framework.serializers import ModelSerializer
from domains.models import *

class DomainSerializer(ModelSerializer):
    
    class Meta:
        model = Domain
        fields = ['title', 'price', 'user']

