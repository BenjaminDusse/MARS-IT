from rest_framework.serializers import ModelSerializer
from domains.models import *

class DomainSerializer(ModelSerializer):
    
    class Meta:
        model = Domain
        fields = ['title', 'price', 'user']

class UserPlanFeature(ModelSerializer):
    
    class Meta:
        model = UserPlanFeature
        fields = ['name', 'user_plan']
        
class UserPlanSerializer(ModelSerializer):
    features = UserPlanFeature(many=True)
    
    class Meta:
        model = UserPlan
        fields = ['title', 'price', 'discount', 'is_recommended', 'features']
        
