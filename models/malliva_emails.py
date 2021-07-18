from mongoengine import fields
from mongoengine.document import Document

# Create your models here.

# capture sent emails and templates


class Email(Document):
    id = fields.SequenceField(primary_key=True)
    content = fields.StringField(max_length=200)
