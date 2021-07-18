from django.db import fields
from mongoengine import fields
from mongoengine.document import Document

# Create your fields here.


class PaymentGateway(Document):
    """
    This model should hand all payment gateways available in a marketplace
    and stores active payments in the marketplace.
    """

    id = fields.SequenceField(primary_key=True)
    handler_name = fields.StringField(max_length=200, blank=False)
    active = fields.BooleanField(default=False)
