from django.db import models
from threadlocals.threadlocals import get_request_variable
from translations.models import Translatable
from django.contrib.auth import get_user_model

User = get_user_model()


def listing_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/domain/listings/<listing id>/<filename>
    return "{0}/{1}/{2}/{3}".format(
        get_request_variable("malliva_domain"),
        "listings",
        instance.listing.id,
        filename,
    )


class Listing(Translatable):
    """
    Listings should belong to more than one categories
    """

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    price = models.IntegerField(blank=False)
    posted_by = models.ForeignKey(
        User, related_name="posted_by", on_delete=models.CASCADE, blank=False
    )
    category = models.ForeignKey(
        "categories.category", on_delete=models.SET_DEFAULT, default="1"
    )
    description = models.CharField(max_length=500, default="")
    visible = models.BooleanField(
        default=True, help_text="Is this listing visible to the public?"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class TranslatableMeta:

        fields = ["title", "description"]


class ListingImage(models.Model):
    """
    Store listing images
    """

    id = models.BigAutoField(primary_key=True)
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="listing_images"
    )
    image = models.ImageField(upload_to=listing_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
