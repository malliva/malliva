from rest_framework import exceptions, viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage

# from .models import User
from django.contrib.auth.models import User
from rest_framework.views import APIView

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

    # API endpoint for login


@api_view(["DELETE"])
def logout(request):
    """
    This view requires authentication and will handle logout requests
    """

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


class UserViewSet(viewsets.ViewSet):
    """
    This viewset api requires authentication and will handle all
    user profile update requests
    user profile view requests,
    user delete requests,
    List users requests,
    """

    authentication_classes = [jwtAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return "hello"

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class PasswordUpdateAPIView(APIView):
    """
    This apiview requires authentication and will handle password change requests
    """

    authentication_classes = [jwtAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user

        if request.data["password"] != request.data["password_confirm"]:
            raise exceptions.ValidationError("Passwords do not match")

        serializer = UserSerializer(user, data=request.data, partial=true)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProfilePictureUploadView(APIView):
    authentication_classes = [jwtAuthentication]
    permission_classes = [IsAuthenticated]
    # parser_classes = [MultiPartParser, ]

    def post(self, request):
        file = request.FILES["image"]
        file_name = default_storage.save(file.name, file)
        url = default_storage.url(file_name)

        return Response({"url": "http://localhost:8000/api" + url})
