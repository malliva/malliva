from uuid import uuid4
from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.


class Transaction(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid4)
    payment_gateway = models.CharField(max_length=200)
    customer_name = models.ForeignKey("mallivaUsers.User", on_delete=DO_NOTHING)
    # paid_to = models.ForeignKey("mallivaUsers.User", on_delete=DO_NOTHING)
