from django.urls import path, re_path
from .views import (
    register,
    login,
    logout,
    UserViewSet,
    PasswordUpdateAPIView,
    ProfilePictureUploadView,
)

urlpatterns = [
    path("register", register),
    path("login", login),
    path("logout", logout),
    path("change_password", PasswordUpdateAPIView.as_view()),
    path("profile_picture", ProfilePictureUploadView.as_view()),
    path("", UserViewSet.as_view({"get": "list"})),
    path(
        "<str:pk>",
        UserViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
]
