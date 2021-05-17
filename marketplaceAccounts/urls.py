from django.urls import path, re_path
from .views import create_marketplace

urlpatterns = [
    re_path(r"^create", create_marketplace),
]
