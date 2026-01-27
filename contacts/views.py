from tkinter.font import names

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
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

class ContactCreate(APIView):
    def post(self,request):
        serializer = ContactsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ContactDetail(APIView):
    def get(self,ruquest,pk):
        contact = get_object_or_404(Contacts,id=pk)
        serializer = ContactsSerializer(contact)
        return Response(serializer.data)

class ContactDelete(APIView):
    def delete(self,request,pk):
        contact = get_object_or_404(Contacts,id=pk)
        contact.delete()
        return Response({'Contact':'Deleted'})






