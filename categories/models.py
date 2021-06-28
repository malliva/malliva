from mongoengine import Document, EmbeddedDocument, fields, queryset
from datetime import datetime

from translations.models import Translatable

# Create your models here.


class Category(Document):
    """
    TODO: Remember to create a default category with fixtures
    """
    category_name = fields.StringField(max_length=200)
    created_at = fields.DateTimeField(default=datetime.utcnow())
    updated_at = fields.DateTimeField(default=datetime.utcnow())
