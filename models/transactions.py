from mongoengine import Document, fields
from mongoengine.queryset.base import CASCADE, DO_NOTHING
from .malliva_users import User

# Create your models here.


class Transaction(Document):
    id = fields.SequenceField(primary_key=True)
    payment_gateway = fields.StringField(max_length=200)
    customer_name = fields.ReferenceField(User, reverse_delete_rule=DO_NOTHING)
    paid_to = fields.ReferenceField(User, reverse_delete_rule=DO_NOTHING)
    order = fields.ForeignKey("orders.Order", reverse_delete_rule=CASCADE)
