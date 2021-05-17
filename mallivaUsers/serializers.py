# middleware to handle user operations before saving in the database

from rest_framework import serializers
from .models import User

from django.conf import settings

# initialize database connections - default to main database
# from tenant_connections import connect_to_database
# connect_to_database(settings.PLATFORM_DB_HOST, settings.PLATFORM_DB_CONN_ALIAS, settings.PLATFORM_DB, settings.DB_USERNAME, settings.DB_PASSWORD)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        # fields = '__all__'
        # allow only selected inputs
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "role",
            "user_context",
        ]

        # Don't show passwords in API responses
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        # remove and return password from validated data
        password = validated_data.pop("password", None)

        user = self.Meta.model(**validated_data)

        if password is not None:
            user.set_password(password)

        user.save()
        return user

    # def update(self, user, validated_data):

    #     # remove and return password from validated data
    #     password = validated_data.pop("password", None)

    #     if password is not None:
    #         user.set_password(password)

    #     user.save()
    #     return user
