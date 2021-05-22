from django.urls import path, re_path
from .views import register, login, logout, UserViewSet, PasswordUpdateAPIView

urlpatterns = [
    re_path(r"^register", register),
    re_path(r"^login", login),
    re_path(r"^login", logout),
    path("users", UserViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "users/<str:pk>",
        UserViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path("users/change_password", PasswordUpdateAPIView.as_view()),
]
