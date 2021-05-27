from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.db.models.deletion import CASCADE, SET_DEFAULT

User = get_user_model()


class Listing(models.Model):
    """
    Listings should belong to more than one categories
    """

    listing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing_name = models.CharField(max_length=200)
    price = models.IntegerField(blank=False)
    posted_by = models.ForeignKey(User, on_delete=CASCADE)
    category = models.ForeignKey(
        "categories.category", on_delete=SET_DEFAULT, default="general"
    )
    created_at = models.DateField(auto_now_add=True)
