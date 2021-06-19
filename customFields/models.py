from django.db import models
from translations.models import Translatable
from threadlocals.threadlocals import get_request_variable
from mallivaUsers.models import User
from listings.models import Listing

# Create your models here.


def field_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/domain/<username>/listings/<filename>
    return "{0}/{1}/{2}".format(
        get_request_variable("malliva_domain"),
        "customfields",
        filename,
    )


class CustomField(Translatable):
    """
    This will allow users create new custom fields for User or listing models
    """

    customFieldType = models.TextChoices(
        "customFieldType", "DROPDOWN TEXT NUMBER LOCATION DATE FILE"
    )

    # associatedModel = models.TextChoices("associatedModel", "USER LISTING")

    id = models.BigAutoField(primary_key=True)
    field_name = models.CharField(max_length=200)
    field_type = models.CharField(
        max_length=200, choices=customFieldType.choices, blank=False
    )
    options = models.CharField(max_length=1000, default="")
    user_field = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    listing_field = models.OneToOneField(Listing, on_delete=models.CASCADE, null=True)
    is_required = models.BooleanField(default=False)
    visible = models.BooleanField(
        default=True, help_text="Is this field visible to the public?"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return description of field
        return self.field_name

    class TranslatableMeta:

        fields = ["field_name"]


class CustomFieldItem(Translatable):
    """
    This will store the content of every created content fields per user or listing
    TODO: Remember content may work as a json field better
    """

    id = models.BigAutoField(primary_key=True)
    custom_field = models.ForeignKey(CustomField, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    file_upload = models.FileField(upload_to=field_directory_path, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class TranslatableMeta:

        fields = ["content"]
