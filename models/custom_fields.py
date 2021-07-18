from enum import Enum
from mongoengine import Document, fields
from mongoengine.queryset.base import CASCADE
from .malliva_users import User
from .listings import Listing
from schema.custom_fields import CustomFieldType, AssociatedModel

# Create your models here.


class CustomField(Document):
    """
    This will allow users create new custom fields for User or listing models
    """

    id = fields.SequenceField(primary_key=True)
    field_name = fields.StringField(max_length=200)
    field_type = fields.EnumField(
        CustomFieldType, default=CustomFieldType.TEXT)
    associated_model = fields.EnumField(AssociatedModel, blank=False)
    user = fields.ReferenceField(User, on_delete=CASCADE, null=True)
    listing = fields.ReferenceField(
        Listing, reverse_delete_rule=CASCADE, null=True)
    is_required = fields.BooleanField(default=False)
    visible = fields.BooleanField(default=True)
    created_at = fields.DateTimeField(auto_now_add=True)
    updated_at = fields.DateTimeField(auto_now=True)


class CustomFieldItem(Document):
    """
    This will store the content of every created content fields per user or listing
    """

    id = fields.SequenceField(primary_key=True)
    custom_field = fields.ReferenceField(
        CustomField, reverse_delete_rule=CASCADE)
    content = fields.DynamicField(max_length=1000, default="")
    created_at = fields.DateTimeField(auto_now_add=True)
    updated_at = fields.DateTimeField(auto_now=True)
