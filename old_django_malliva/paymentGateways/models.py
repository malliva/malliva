from django.db import models

# Create your models here.
class PaymentGateway(models.Model):
    """
    This model should hand all payment gateways available in a marketplace
    and stores active payments in the marketplace.
    """

    id = models.BigAutoField(primary_key=True)
    handler_name = models.CharField(
        max_length=200, blank=False, help_text="Name of the payment gateway"
    )
    active = models.BooleanField(default=False)
