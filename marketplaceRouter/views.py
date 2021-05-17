from django.shortcuts import render
from rest_framework import viewsets, exceptions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

# from .authentication import generate_access_token, jwtAuthentication
from .serializers import MarketplaceSerializer

# Create your views here.


@api_view(["GET"])
def router(request):
    return Response("It works")


@api_view(["POST"])
def create_marketplace(request):
    data = request.data

    serializer = MarketplaceSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
