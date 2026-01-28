from tkinter.font import names

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from contacts.models import Contacts
from .serializers import ContactsSerializer
from rest_framework.decorators import api_view



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
    def get(self,request,pk):
        contact = get_object_or_404(Contacts,id=pk)
        serializer = ContactsSerializer(contact)
        return Response(serializer.data)

class ContactDelete(APIView):
    def delete(self,request,pk):
        contact = get_object_or_404(Contacts,id=pk)
        contact.delete()
        return Response({'Contact':'Deleted'})

class ContactUpdate(APIView):
    def put(self,request,pk):
        contact = get_object_or_404(Contacts,id=pk)
        serializer = ContactsSerializer(contact,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

#FBV -> Function based view  @decorator mn ishteit
@api_view(['GET'])
def contact_list_fbv(request):
    contacts = Contacts.objects.all()
    serializer = ContactsSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def contact_create_fbv(request):
    serializer = ContactsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def contact_update_fbv(request, pk):
    contact = get_object_or_404(Contacts,id=pk)
    serializer = ContactsSerializer(contact, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Delete'])
def contact_delete_fbv(request,pk):
    contact = get_object_or_404(Contacts,id=pk)
    contact.delete()
    return Response({'Contact:' :'Deleted'})




