# middleware to handle user operations before saving in the database

import rest_framework_mongoengine import serializers
from .models import User

from django.conf import settings

from tenant_connections import connect_to_database
connect_to_database(settings.PLATFORM_DB_HOST, settings.PLATFORM_DB_CONN_ALIAS, settings.PLATFORM_DB, settings.DB_USERNAME, settings.DB_PASSWORD)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = '__all__'

    
