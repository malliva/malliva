from re import I
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User

from .authentication import generate_access_token, jwtAuthentication
from .serializers import UserSerializer


# Create your views here.


@api_view(["POST"])
def register(request):

    data = request.data

    if data["password"] != data["password_confirm"]:
        raise exceptions.APIException("Passwords do not match")

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


# API endpoint for login
@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = User.objects.filter(email=email).first()

    if user is None:
        raise exceptions.AuthenticationFailed("User not found!")

    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("Incorrect Password!")

    response = Response("success")

    token = generate_access_token(user)
    response.set_cookie(key="jwt", value=token, httponly=True)

    response.data = {"jwt": token}

    return response
