from django.db import models
import uuid
from threadlocals.threadlocals import get_request_variable
from translations.models import Translatable

from django.contrib.auth import get_user_model

User = get_user_model()


def listing_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/domain/<username>/listings/<filename>
    return "{0}/{1}/{2}/{3}".format(
        get_request_variable("malliva_domain"),
        instance.username,
        "listings",
        filename,
    )


class Listing(Translatable):
    """
    Listings should belong to more than one categories
    """

    listing_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False
    )
    listing_name = models.CharField(max_length=200)
    price = models.IntegerField(blank=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(
    #    "categories.category", on_delete=models.SET_DEFAULT, default="general"
    # )
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class TranslatableMeta:
        fields = ["category", "description"]

    @property
    def set_posted_by(self, user):
        """
        set author of this listing
        """
        self.posted_by = user


class ListingImage(models.Model):
    """
    Store listing images
    """

    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="listing_images"
    )
    images = models.ImageField(upload_to=listing_directory_path, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def set_listing(self):
        """
        set listing for this image
        """
