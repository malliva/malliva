from django.contrib.auth import models
from rest_framework_mongoengine import serializers
from .models import Listing, ListingImage
from django.http import QueryDict


class ListingImageSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = ListingImage
        depth = 2
        fields = ["image"]


class ListingSerializer(serializers.DocumentSerializer):
    listing_images = ListingImageSerializer(
        ListingImage, many=True, required=False)

    class Meta:
        model = Listing
        depth = 2

        # allow only selected inputs
        fields = [
            "title",
            "price",
            "description",
            "posted_by",
            "category",
            "listing_images",
        ]

    def create(self, validated_data):

        images = validated_data.pop("listing_images", None)
        listing = Listing.objects.create(**validated_data)
        listing.listing_images = []
        print(images)
        if images is not None:
            for image in images:
                listing.listing_images.append(image)
        listing.save()

        return listing

    # def update(self, instance, validated_data):

    #     instance.listing_name = validated_data.get(
    #         "listing_name", instance.listing_name
    #     )
    #     instance.price = validated_data.get("price", instance.price)
    #     instance.category = validated_data.get("category", instance.category)
    #     instance.description = validated_data.get("description", instance.description)
    #     instance.save()
    #     return instance
