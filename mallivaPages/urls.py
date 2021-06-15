from django.urls import path, re_path
from .views import index
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Pastebin API")

urlpatterns = [re_path("", schema_view)]
