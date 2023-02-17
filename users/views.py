from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.decorators import action
from users.serializers import ContactSerializer, CustomUserSerializer, UserPlanSerializer, ContactCreateSerializer
from users.models import CustomUser, Contact, UserPlan


class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ContactCreateSerializer
        elif self.request.method == 'GET':
            return ContactSerializer
        return ContactSerializer

class ContactDetail(APIView):
    def get_object(self, chat_id):
        try:
            return Contact.objects.get(chat_id=chat_id)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, chat_id, format=None):
        snippet = self.get_object(chat_id)
        serializer = ContactSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, chat_id, format=None):
        snippet = self.get_object(chat_id)
        serializer = ContactSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, chat_id, format=None):
        snippet = self.get_object(chat_id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class CustomUserViewSet(viewsets.ModelViewSet):
    
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserPlanViewSet(viewsets.ModelViewSet):
    
    queryset = UserPlan.objects.all()
    serializer_class = UserPlanSerializer

    