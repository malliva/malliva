from django.urls import path, re_path
from .views import register, login

urlpatterns = [re_path(r"^register", register), re_path(r"^login", login)]
