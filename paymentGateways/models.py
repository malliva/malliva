from django.db import models
import uuid

# Create your models here.
class PaymentGateway(models.Model):
    """
    This model should hand all payment gateways available in a marketplace
    and stores active payments in the marketplace.
    """

    gateway_id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4()
    )
    handler_name = models.CharField(
        max_length=200, blank=False, help_text="Name of the payment gateway"
    )
    active = models.BooleanField(default=False)
