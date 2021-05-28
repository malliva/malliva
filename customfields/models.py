import uuid
from django.db import models
from django.db.models.deletion import PROTECT
from threadlocals.threadlocals import get_request_variable

# Create your models here.


def field_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/domain/<username>/<filename>
    return "{0}/{1}/{2}".format(
        get_request_variable("malliva_domain"), instance.username, filename
    )


class CustomField(models.Model):

    customFieldType = models.TextChoices(
        "customFieldType", "DROPDOWN TEXT NUMBER LOCATION DATE FILE"
    )
    associatedModel = models.TextChoices("associatedModel", "USER LISTING")

    field_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    field_name = models.CharField(max_length=200)
    field_type = models.CharField(max_length=200, choices=customFieldType.choices)
    associated_model = models.CharField(max_length=200, choices=associatedModel.choices)
    is_required = models.BooleanField(default=False)
    public = models.BooleanField(default=True)


class CustomFieldItem(models.Model):
    """
    This will store the content of every created content fields per user or listing
    TODO: Remember content may work as a json field better
    """

    field_content_id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    custom_field = models.ForeignKey(CustomField, on_delete=PROTECT)
    field_content = models.CharField(
        max_length=200,
    )
    field_upload = models.FileField(upload_to=field_directory_path, default="")
