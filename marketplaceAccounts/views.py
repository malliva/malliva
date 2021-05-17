from django.shortcuts import render
from rest_framework import viewsets, exceptions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

# from .authentication import generate_access_token, jwtAuthentication
from .serializers import MarketplaceAccountSerializer

from django.contrib.sites.shortcuts import get_current_site


@api_view(["POST"])
def create_marketplace(request):
    data = request.data
    current_site = get_current_site(request)
    print(current_site)

    serializer = MarketplaceAccountSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
