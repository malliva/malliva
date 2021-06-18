from rest_framework import exceptions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from .authentication import generate_access_token, jwtAuthentication
from .serializers import UserSerializer, PermissionSerializer, RoleSerializer
from .models import User, Permission, Role
from .permissions import ViewPermissions


@api_view(["POST"])
def register(request):

    """
    API endpoint for user account registrations
    """

    data = request.data

    if data["password"] != data["password_confirm"]:
        raise exceptions.APIException("Passwords do not match")

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def login(request):

    """
    API endpoint for user authentication
    """

    email = request.data.get("email")
    password = request.data.get("password")

    user = User.objects.filter(email=email).first()

    if user is None or user.is_active is not True:
        raise exceptions.AuthenticationFailed("User not found!")

    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("Incorrect Password!")

    response = Response("success")

    token = generate_access_token(user)
    response.set_cookie(key="jwt", value=token, httponly=True)

    response.data = {"jwt": token}

    return response


@api_view(["POST"])
def logout(request):

    """
    API endpoint for user logout
    """
    response = Response()
    response.delete_cookie(key="jwt")

    response.data = {"message": "Logout Successful"}

    return response


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

        # initialize the serializer
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # call the serializer
        serializer.save(owner=user)
        return Response(serializer.data)


# class ProfilePictureUploadView(viewsets.ViewSet):
#     """
#     This viewset api requires authentication and will handle all
#     user profile update requests
#     user profile view requests,
#     user delete requests,
#     List users requests,
#     """

#     authentication_classes = [jwtAuthentication]
#     permission_classes = [IsAuthenticated]

#     parser_classes = [MultiPartParser]

#     def upload(self, request):

#         user = request.user

#         serializer = UserSerializer(user, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data)


@api_view(["POST"])
def forgot_password(request):

    """
    API endpoint for users that want to remember password
    """

    data = request.data

    if data["password"] != data["password_confirm"]:
        raise exceptions.APIException("Passwords do not match")

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


# class ListUsers(APIView):
#     """
#     View to list all users in the marketplace.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """

#     authentication_classes = [jwtAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)


class UserViewSet(viewsets.ViewSet):
    """
    This viewset api requires authentication and will handle all
    user profile update requests
    user profile view requests,
    user delete requests
    """

    authentication_classes = [jwtAuthentication]
    permission_classes = [IsAuthenticated]

    parser_classes = [
        MultiPartParser,
    ]

    queryset = User.objects.all()

    def retrieve(self, request, pk=None):

        if pk:
            try:
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except:
                response = Response()
                response.data = {"message": "wrong user id provided"}
                response.status_code = status.HTTP_404_NOT_FOUND
                return response
        else:
            serializer = UserSerializer(self.queryset, many=True)
            return Response(serializer.data)

    def update_user(self, request, pk=None):

        user = request.user

        # initialize the serializer
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # call the serializer
        serializer.save(owner=user)

        return Response(serializer.data)

    def destroy_user(self, request, pk=None):

        user = request.user
        user.soft_delete()
        user.save()

        response = Response()
        response.delete_cookie(key="jwt")
        response.data = {"message": "User was successfully deleted"}

        return response


class PermissionAPIView(APIView):
    """
    View all available permissions
    """

    authentication_classes = [jwtAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)

        return Response({"data": serializer.data})


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [jwtAuthentication]
    permission_classes = [IsAuthenticated & ViewPermissions]
    permission_object = "roles"

    def list(self, request):
        serializer = RoleSerializer(Role.objects.all(), many=True)

        return Response({"data": serializer.data})

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)

        return Response({"data": serializer.data})

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data": serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
