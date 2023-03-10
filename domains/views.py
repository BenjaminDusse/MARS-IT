from rest_framework import viewsets

from domains.models import *
from domains.serializers import *

class DomainViewSet(viewsets.ModelViewSet):
    
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

