from mongoengine import fields, Document
from mongoengine.queryset.base import DO_NOTHING
from .malliva_users import User
# Create your models here.


class Message(Document):
    id = fields.SequenceField(primary_key=True)
    initiated_by = fields.ReferenceField(User, reverse_delete_rule=DO_NOTHING)
    received_by = fields.LazyReferenceField(User, on_delete=DO_NOTHING)
