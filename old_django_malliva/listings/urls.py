from django.urls import path, re_path
from .views import ListingViewSet

urlpatterns = [
    path("create", ListingViewSet.as_view({"post": "create"})),
    path(
        "<str:pk>",
        ListingViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update_listing",
                "delete": "destroy_listing",
            }
        ),
    ),
    path("", ListingViewSet.as_view({"get": "retrieve"})),
]
