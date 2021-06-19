from rest_framework import serializers
from .models import CustomField, CustomFieldItem

from mallivaUsers.models import User
from listings.models import Listing

from listings.serializers import ListingSerializer
from mallivaUsers.serializers import UserSerializer


# class AssociatedModelRelatedField(serializers.RelatedField):
#     """
#     A custom field to use for the `tagged_object` generic relationship.
#     """

#     def to_representation(self, value):
#         """
#         Serialize bookmark instances using a bookmark serializer,
#         and note instances using a note serializer.
#         """
#         if isinstance(value, User):
#             serializer = UserSerializer(value)
#         elif isinstance(value, Listing):
#             serializer = ListingSerializer(value)
#         else:
#             raise Exception("Unexpected type of tagged object")

#         return serializer.data


class CustomFieldItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFieldItem
        fields = ["custom_field", "field_content", "field_upload"]


class CustomFieldSerializer(serializers.ModelSerializer):
    custom_field_items = CustomFieldItemSerializer(many=True, required=False)

    assoc

    class Meta:
        model = CustomField

        # allow only selected inputs
        fields = [
            "field_name",
            "field_type",
            "options",
            "content_type",
            "associated_mModel",
            "is_required",
            "visible",
            "custom_field_items",
        ]
