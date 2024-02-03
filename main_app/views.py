from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Calls, Clients, Medics
from .serializer import CallsSerializer, ClientsSerializer, MedicsSerializer


class ClientsCreate(generics.CreateAPIView):
    queryset = Clients.objects.all() 
    serializer_class = ClientsSerializer

class CallsCreate(generics.CreateAPIView):
    queryset = Calls.objects.all()
    serializer_class = CallsSerializer


class MedicsRetrieve(generics.RetrieveAPIView):
    queryset = Medics.objects.all()
    serializer_class = MedicsSerializer

