from django.contrib.auth import models
from rest_framework import serializers
from .models import Listing, ListingImage


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing

        # fields = '__all__'
        # allow only selected inputs
        fields = ["listing_name", "price", "description"]

    def create(self, validated_data):

        listing = self.Meta.model(**validated_data)
        # listing.set_posted_by(user)

        listing.save()
        return listing

    def update(self, instance, validated_data):

        instance.listing_name = validated_data.get(
            "listing_name", instance.listing_name
        )
        instance.price = validated_data.get("price", instance.price)
        instance.category = validated_data.get("category", instance.category)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance


class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = "__all__"
