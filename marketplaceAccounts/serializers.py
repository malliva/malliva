# middleware to initial marketplace accounts after user signups

from rest_framework import serializers
from .models import MarketplaceAccount


class MarketplaceAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketplaceAccount

        # allow only selected fields
        fields = ["marketplace_name", "subdomain"]

    def create(self, validated_data):
        marketplace = MarketplaceAccount(
            marketplace_name=validated_data["marketplace_name"],
            subdomain=validated_data["subdomain"].replace(" ", "").lower(),
            database_name=validated_data["subdomain"].replace(" ", "").lower(),
        )

        marketplace.save()
        return marketplace
