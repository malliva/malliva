from mongoengine import Document, EmbeddedDocument, fields, queryset
from datetime import datetime

# Create your models here.


class Category(Document):
    """
    TODO: Remember to create a default category with fixtures
    """
    name = fields.StringField(max_length=200)
    created_at = fields.DateTimeField(default=datetime.utcnow())
    updated_at = fields.DateTimeField(default=datetime.utcnow())
