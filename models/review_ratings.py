from mongoengine import fields
from mongoengine.document import Document
from mongoengine.queryset.base import DO_NOTHING
from .malliva_users import User

# Create your models here.


class reviewRating(Document):
    id = fields.SequenceField(primary_key=True)
    giver = fields.ReferenceField(User, reverse_delete_rule=DO_NOTHING)
    receiver = fields.ReferenceField(User, reverse_delete_rule=DO_NOTHING)
