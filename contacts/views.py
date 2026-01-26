from tkinter.font import names

from rest_framework.views import APIView #get API tuzuu uchun k.k
from rest_framework.response import Response #json formatta kaitar
from contacts.models import Contacts
from .serializers import ContactsSerializer



class Hello(APIView):
    def get(self, request):
        return Response({'message': 'Men jazgan API'})

class Goodbye(APIView):
    def get(self, request):
        return Response({'message': 'GOODBYE World'})

class Hi(APIView):
    def get(self, request):
        return Response({'text':'Hi API!'})

class Stud(APIView):
    def get(self,request):
        return Response({'Student': 'Ailin'})

class Info(APIView):
    def get(self,reguest):
        return Response({"developer":"name",
                         "project":"Contacts API"})

class ContactList(APIView):
    def get(self,request):
        contacts = Contacts.objects.all()
        serializer = ContactsSerializer(contacts, many=True)
        return Response(serializer.data)





