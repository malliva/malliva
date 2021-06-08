from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, exceptions
from rest_framework.parsers import MultiPartParser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from mallivaUsers.authentication import jwtAuthentication
from .serializers import ListingSerializer
from .models import Listing

# Create your views here.
class ListingViewSet(viewsets.ViewSet):
    """
    This viewset api requires authentication and will handle all
    listing creation requests
    listing update requests
    listing view requests,
    listing delete requests
    """

    authentication_classes = [jwtAuthentication]
    permission_classes = [IsAuthenticated]

    parser_classes = [
        MultiPartParser,
    ]

    def create_listing(self, request, pk=None):

        user = request.user
        data = request.data

        serializer = ListingSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        user = request.user

        queryset = Listing.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ListingSerializer(user)
        return Response(serializer.data)

    def update_listing(self, request, pk=None):

        user = request.user

        # initialize the serializer
        serializer = ListingSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # call the serializer
        serializer.save(owner=user)

        return Response(serializer.data)

    def destroy_listing(self, request, pk=None):

        user = request.user
        listing = request.listing
        listing.delete()

        response = Response()
        response.data = {"message": "Listing was successfully deleted"}

        return response


class ShowListings(APIView):
    """
    Show all listings permitted by this user.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    authentication_classes = [jwtAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of listings.
        """
        queryset = Listing.objects.all()
        serializer = ListingSerializer(queryset, many=True)
        return Response(serializer.data)
