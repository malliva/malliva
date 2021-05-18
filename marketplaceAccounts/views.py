from django.shortcuts import render
from rest_framework import viewsets, exceptions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

# from .authentication import generate_access_token, jwtAuthentication
from .serializers import MarketplaceAccountSerializer


@api_view(["POST"])
def create_marketplace(request):
    data = request.data

    # set the database for this request
    database_name = request.META["database_name"]
    print(database_name)

    serializer = MarketplaceAccountSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
