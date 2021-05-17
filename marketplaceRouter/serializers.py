# middleware to handle user operations before saving in the database

from rest_framework import serializers
from .models import MarketplaceRouter

from django.conf import settings

# initialize database connections - default to main database
# from tenant_connections import connect_to_database
# connect_to_database(settings.PLATFORM_DB_HOST, settings.PLATFORM_DB_CONN_ALIAS, settings.PLATFORM_DB, settings.DB_USERNAME, settings.DB_PASSWORD)


class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketplaceRouter

        # fields = '__all__'
        # allow only selected inputs
        fields = [
            "marketplace_name",
            "identity",
            "marketplace_domain",
            "use_domain",
            "marketplace_version",
        ]

    def create(self, validated_data):

        marketplace = self.Meta.model(**validated_data)

        marketplace.save()
        return marketplace
