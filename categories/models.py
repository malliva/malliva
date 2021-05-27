from django.db import models
import uuid

# Create your models here.
class Category(models.Model):
    """
    TODO: Remember to set a default category
    """

    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
