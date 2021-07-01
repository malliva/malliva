# middleware to initial marketplace accounts after user signups

from rest_framework import serializers
from .models import Plan, Subscription, MarketplaceAccount


class Plan(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class Subscription(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class MarketplaceAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketplaceAccount

        # allow only selected fields
        fields = [
            "owner",
            "marketplace_name",
            "subdomain",
            "domain",
            "use_domain",
            "configuration",
            "subscription",
        ]

    # def create(self, validated_data):
    #     marketplace = MarketplaceAccount(
    #         marketplace_name=validated_data["marketplace_name"],
    #         subdomain=validated_data["subdomain"].replace(" ", "").lower(),
    #         database_name=validated_data["subdomain"].replace(" ", "").lower(),
    #     )

    #     marketplace.save()
    #     return marketplace
