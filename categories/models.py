from django.db import models

from translations.models import Translatable

# Create your models here.
class Category(Translatable):
    """
    TODO: Remember to create a default category with fixtures
    """

    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

    class TranslatableMeta:

        fields = ["category_name"]
