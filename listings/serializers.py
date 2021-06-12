from django.contrib.auth import models
from rest_framework import serializers
from .models import Listing, ListingImage
from django.http import QueryDict


class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ["image", "listing"]
        extra_kwargs = {"listing": {"write_only": True}}


class ListingSerializer(serializers.ModelSerializer):
    listing_images = ListingImageSerializer(many=True, required=False)

    class Meta:
        model = Listing

        # allow only selected inputs
        fields = [
            "title",
            "price",
            "description",
            "posted_by",
            "category",
            "listing_images",
        ]

    # def create(self, validated_data):
    #     print(validated_data)
    #     images = validated_data.pop("listing_images", None)

    #     listing = Listing.objects.create(**validated_data)

    #     if images is not None:
    #         print("finally worked")
    #         for listing_image in images:
    #             ListingImage.objects.create(listing=listing, **listing_image)

    #     return listing

    # def update(self, instance, validated_data):

    #     instance.listing_name = validated_data.get(
    #         "listing_name", instance.listing_name
    #     )
    #     instance.price = validated_data.get("price", instance.price)
    #     instance.category = validated_data.get("category", instance.category)
    #     instance.description = validated_data.get("description", instance.description)
    #     instance.save()
    #     return instance
