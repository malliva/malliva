from django.urls import path, re_path
from .views import ListingViewSet, ShowListings

urlpatterns = [
    path(
        "<str:pk>",
        ListingViewSet.as_view(
            {
                "post": "create_listing",
                "get": "retrieve",
                "put": "update_listing",
                "delete": "destroy_listing",
            }
        ),
    ),
    path("", ShowListings.as_view()),
]
