from mongoengine import Document, fields, queryset, EmbeddedDocument, EmbeddedDocumentListField
from datetime import datetime
from .malliva_users import User


class ListingImage(EmbeddedDocument):
    """
    Store listing images
    """
    id = fields.SequenceField(primary_key=True)
    image = fields.StringField()


class Listing(Document):
    """
    Listings should belong to more than one categories
    """
    id = fields.SequenceField(primary_key=True)
    title = fields.StringField(max_length=200)
    price = fields.FloatField(min_value=0.0)
    posted_by = fields.ReferenceField(
        User, reverse_delete_rule=queryset.CASCADE)
    # category = fields.ReferenceField(Category, reverse_delete_rule=queryset.DO_NOTHING)
    description = fields.StringField(max_length=500, default="")
    listing_images = fields.EmbeddedDocumentListField(
        ListingImage, required=False)
    visible = fields.BooleanField(
        default=True,  # help_text="Is this listing visible to the public?"
    )
    created_at = fields.DateTimeField(default=datetime.utcnow())
    updated_at = fields.DateTimeField(default=datetime.utcnow())
