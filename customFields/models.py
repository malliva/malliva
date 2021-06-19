from django.db import models
from translations.models import Translatable
from threadlocals.threadlocals import get_request_variable
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


def field_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/domain/<username>/listings/<filename>
    return "{0}/{1}/{2}".format(
        get_request_variable("malliva_domain"),
        "customfields",
        filename,
    )


class CustomField(models.Model):
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
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    associatedModel = GenericForeignKey("content_type", "object_id")
    is_required = models.BooleanField(default=False)
    visible = models.BooleanField(
        default=True, help_text="Is this field visible to the public?"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return description of field
        return self.field_name


class CustomFieldItem(Translatable):
    """
    This will store the content of every created content fields per user or listing
    TODO: Remember content may work as a json field better
    """

    id = models.BigAutoField(primary_key=True)
    custom_field = models.ForeignKey(CustomField, on_delete=models.CASCADE)
    field_content = models.CharField(
        max_length=500,
    )
    field_upload = models.FileField(upload_to=field_directory_path, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class TranslatableMeta:

        fields = ["field_content"]
