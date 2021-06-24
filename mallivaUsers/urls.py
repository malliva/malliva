from django.urls import path, re_path
from .views import (
    register,
    login,
    logout,
    UserViewSet,
    MarketplaceUserViewSet,
    PasswordUpdateAPIView,
)

urlpatterns = [
    path("register", register),
    path("login", login),
    path("logout", logout),
    path("change_password", PasswordUpdateAPIView.as_view()),
    path(
        "<str:pk>",
        UserViewSet.as_view(
            {"get": "retrieve", "put": "update_user", "delete": "destroy_user"}
        ),
    ),
    path(
        "<str:pk>",
        MarketplaceUserViewSet.as_view(
            {"get": "retrieve", "put": "update_user", "delete": "destroy_user"}
        ),
    ),
    path("", UserViewSet.as_view({"get": "retrieve"})),
]
