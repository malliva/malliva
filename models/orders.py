from .malliva_users import User
from .listings import Listing, ListingImage
from mongoengine import fields
from mongoengine.document import Document
from mongoengine.queryset.base import DO_NOTHING
from .payment_gateways import PaymentGateway


class Order(Document):
    """
    This model should hand all orders and payments in the marketplace.

    TODO: set orders belonging to deleted user to "deleted user"
    """

    id = fields.SequenceField(primary_key=True)
    PaymentGateway = fields.ReferenceField(
        PaymentGateway, reverse_delete_rule=DO_NOTHING)
    listing = fields.ReferenceField(Listing)
    seller = fields.ReferenceField(
        User, reverse_delete_rule=DO_NOTHING, default="deleted_user")
    buyer = fields.LazyReferenceField(
        User, reverse_delete_rule=DO_NOTHING, default="deleted_user")
