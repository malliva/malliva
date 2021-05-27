from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.db.models.deletion import SET_DEFAULT

User = get_user_model()

# Create your models here.
class Order(models.Model):
    """
    This model should hand all orders and payments in the marketplace.

    TODO: set orders belonging to deleted user to "deleted user"
    """

    order_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    PaymentGateway = models.ForeignKey("paymentGateways.PaymentGateway")
    seller = models.ForeignKey(
        User, on_delete=SET_DEFAULT, default="deleted_user", blank=False
    )
    buyer = models.ForeignKey(
        User, on_delete=SET_DEFAULT, default="deleted_user", blank=False
    )
