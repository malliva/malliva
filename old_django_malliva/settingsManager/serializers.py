# middleware to initial marketplace accounts after user signups

from rest_framework import serializers
from .models import SocialMediaPage, Configuration, TemplateStyling


class SocialMediaPage(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaPage
        fields = "__all__"


class TemplateStyling(serializers.ModelSerializer):
    class Meta:
        model = TemplateStyling
        fields = "__all__"


class Configuration(serializers.ModelSerializer):
    # listing_images = ListingImageSerializer(many=True, required=False)

    class Meta:
        model = Configuration

        # allow only selected inputs
        fields = "__all__"
