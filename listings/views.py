from django.core.files.storage import default_storage
from django.http.response import JsonResponse
from django.utils import translation
from django.utils.text import re_words
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, viewsets, status, exceptions
from rest_framework.parsers import MultiPartParser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.http import QueryDict
import os

from mallivaUsers.authentication import jwtAuthentication
from .serializers import ListingSerializer, ListingImageSerializer
from .models import Listing, ListingImage

# Create your views here.


# @api_view(["POST"])
# def create(request):
#     authentication_classes = [jwtAuthentication]
#     permission_classes = [IsAuthenticated]

#     parser_classes = [
#         MultiPartParser,
#     ]

#     data = request.data

#     serializer = ListingSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     listing = Listing.objects.create(**serializer.validated_data)
#     listing.save()
#     try:
#         images = QueryDict.pop(data, "image")
#         for img in images:
#             imageserializer = ListingImageSerializer(
#                 data={"listing": listing.pk, "image": img}
#             )
#             imageserializer.is_valid(raise_exception=True)
#             imageserializer.save()

#         uploaded_images = ListingImage.objects.filter(listing=listing.pk)
#         serialized_images = ListingImageSerializer(uploaded_images, many=True)
#         serialized_listing = serializer.data
#         serialized_listing.update({"listing_images": serialized_images.data})
#         return Response(serialized_listing)
#     except:
#         print("no listing image uploaded")
#         return Response(serializer.data)


class ListingViewSet(viewsets.ViewSet):
    """
    This viewset api requires authentication and will handle all
    listing creation requests
    listing update requests
    listing view requests,
    listing delete requests

    TODO: remember to set permissions
    """

    authentication_classes = [jwtAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Listing.objects.all()

    parser_classes = [
        MultiPartParser,
    ]

    def create(self, request):
        data = request.data

        serializer = ListingSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        listing = Listing.objects.create(**serializer.validated_data)
        listing.save()
        try:
            images = QueryDict.pop(data, "image")
            for img in images:
                imageserializer = ListingImageSerializer(
                    data={"listing": listing.pk, "image": img}
                )
                imageserializer.is_valid(raise_exception=True)
                imageserializer.save()

            uploaded_images = ListingImage.objects.filter(listing=listing.pk)
            serialized_images = ListingImageSerializer(uploaded_images, many=True)
            serialized_listing = serializer.data
            serialized_listing.update({"listing_images": serialized_images.data})
            return Response(serialized_listing)
        except:
            print("no listing image uploaded")
            return Response(serializer.data)

    def retrieve(self, request, pk=None):

        """
        Return a list of listings.
        """
        if pk:
            try:
                listing = Listing.objects.get(pk=pk)
                serializer = ListingSerializer(listing)
                return Response(serializer.data)
            except:
                response = Response()
                response.data = {"message": "wrong listing id provided"}
                response.status_code = status.HTTP_404_NOT_FOUND
                return response
        else:
            serializer = ListingSerializer(self.queryset, many=True)
            return Response(serializer.data)

    def update_listing(self, request, pk=None):

        user = request.user
        data = request.data

        # initialize the serializer
        try:
            listing = Listing.objects.get(pk=pk)
        except:
            response = Response()
            response.data = {"message": "wrong listing id provided"}
            response.status_code = status.HTTP_404_NOT_FOUND
            return response

        serializer = ListingSerializer(listing, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        uploaded_images = ListingImage.objects.filter(listing=listing.pk)
        # serializer.save(owner=user)
        try:
            images = QueryDict.pop(data, "image")
            for img in images:
                for uploadedimg in uploaded_images:

                    print(os.path.basename(uploadedimg.image.name))
                    print(img.name)

                    # Check if images are the same
                    if img.name == os.path.basename(uploadedimg.image.name):
                        print("same image")
                    else:
                        print("different images")
                        imageserializer = ListingImageSerializer(
                            data={"listing": listing.pk, "image": img}
                        )
                        imageserializer.is_valid(raise_exception=True)
                        imageserializer.save()

                        # TODO: handle listing images deleting later in updates
                        # and prevent duplicate uploads, maximum no of images per listing

            serializer.save(owner=user)
            return Response(serializer.data)
        except:
            print("no listing image uploaded")
            serializer.save(owner=user)
            return Response(serializer.data)

    def destroy_listing(self, request, pk=None):
        # TODO: remember to set permissions
        user = request.user

        try:
            listing = Listing.objects.get(pk=pk)
        except:
            response = Response()
            response.data = {"message": "wrong listing id provided"}
            response.status_code = status.HTTP_404_NOT_FOUND
            return response

        listing.delete()

        response = Response()
        response.data = {"message": "Listing was successfully deleted"}

        return response


# class ShowListings(APIView):
#     """
#     Show all listings permitted by this user.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """

#     authentication_classes = [jwtAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         """
#         Return a list of listings.
#         """
#         queryset = Listing.objects.all()
#         serializer = ListingSerializer(queryset, many=True)
#         return Response(serializer.data)
