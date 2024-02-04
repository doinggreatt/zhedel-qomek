from django.shortcuts import render
from rest_framework import generics, status
from .models import Calls, Clients, Medics, Cars
from .serializer import ClientSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import redis, json
from zhedel_qomek import settings
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.forms import model_to_dict
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)


class ClientCreate(APIView):
    def post(self, request):
        serializer= ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_record = Clients.objects.create(
                clientName = request.data['clientName'],
                clientSurname = request.data['clientSurname'],
                phoneNumber = request.data['phoneNumber'],
                password = request.data['password'],
                age = request.data['age'],
                sex = request.data['sex'],
        )

        return Response({'data': ClientSerializer(new_record).data})


