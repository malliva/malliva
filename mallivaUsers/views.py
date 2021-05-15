from django.shortcuts import render
from rest_framework import viewsets, exceptions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .authentication import generate_access_token, jwtAuthentication
from .serializers import UserSerializer

# Create your views here.

@api_view(['POST'])
def register(request):

    data = request.data

    if data['password'] != data['password_confirm']:
        raise exceptions.APIException('Passwords do not match')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)