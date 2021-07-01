from mongoengine import Document, EmbeddedDocument, fields, queryset
from datetime import datetime
from threadlocals.threadlocals import get_request_variable
from translations.models import Translatable
from mallivaUsers.models import User, MarketplaceUser
from categories.models import Category


def listing_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/domain/listings/<listing id>/<filename>
    return "{0}/{1}/{2}/{3}".format(
        get_request_variable("malliva_domain"),
        "listings",
        instance.listing.id,
        filename,
    )


class ListingImage(EmbeddedDocument):
    """
    Store listing images
    """
    image = fields.ImageField()


class Listing(Document):
    """
    Listings should belong to more than one categories
    """
    #id = fields.LongField(min_value=1, primary_key=True)
    title = fields.StringField(max_length=200)
    price = fields.FloatField(min_value=0.0)
    posted_by = fields.ReferenceField(
        User, reverse_delete_rule=queryset.CASCADE)
    category = fields.ReferenceField(
        Category, reverse_delete_rule=queryset.DO_NOTHING)
    description = fields.StringField(max_length=500, default="")
    listing_images = fields.EmbeddedDocumentListField(
        ListingImage, required=False)
    visible = fields.BooleanField(
        default=True,  # help_text="Is this listing visible to the public?"
    )
    created_at = fields.DateTimeField(default=datetime.utcnow())
    updated_at = fields.DateTimeField(default=datetime.utcnow())
