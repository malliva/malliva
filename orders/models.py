from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import DO_NOTHING, SET_DEFAULT

User = get_user_model()

# Create your models here.
class Order(models.Model):
    """
    This model should hand all orders and payments in the marketplace.

    TODO: set orders belonging to deleted user to "deleted user"
    """

    id = models.BigAutoField(primary_key=True)
    PaymentGateway = models.ForeignKey(
        "paymentGateways.PaymentGateway", on_delete=DO_NOTHING
    )
    seller = models.ForeignKey(
        User, on_delete=SET_DEFAULT, default="deleted_user", blank=False
    )
    # buyer = models.ForeignKey(
    #    User, on_delete=SET_DEFAULT, default="deleted_user", blank=False
    # )
