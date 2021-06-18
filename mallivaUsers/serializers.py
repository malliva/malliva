# middleware to handle user operations before saving in the database

from rest_framework import serializers
from .models import User, Permission, Role

from customFields.serializers import CustomFieldSerializer, CustomFieldItemSerializer


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = "__all__"

    def create(self, validated_data):
        permissions = validated_data.pop("permissions", None)
        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.permissions.add(*permissions)
        instance.save()
        return instance


class RoleRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return RoleSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class UserSerializer(serializers.ModelSerializer):
    role = RoleRelatedField(many=False, queryset=Role.objects.all())
    # customfields = CustomFieldObjectRelatedField()

    class Meta:
        model = User

        # fields = '__all__'
        # allow only selected inputs
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "profile_picture",
            # "custom_fields",
            "role",
        ]

        # Don't show passwords in API responses
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        # remove and return password from validated data
        password = validated_data.pop("password", None)

        user = self.Meta.model(**validated_data)

        if password is not None:
            user.set_password(password)

        user.set_username

        user.save()
        return user

    def update(self, instance, validated_data):

        # remove and return password from validated data
        password = validated_data.pop("password", None)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.role = validated_data.get("role", instance.role)
        instance.profile_picture = validated_data.get(
            "profile_picture", instance.profile_picture
        )

        if password is not None:
            instance.set_password(password)

        print(instance.get_fullname)

        instance.save()
        return instance
