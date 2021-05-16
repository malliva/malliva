from django.urls import path, re_path
from .views import router

urlpatterns = [
    path(r"", router),
]
