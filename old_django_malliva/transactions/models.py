from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Transaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    payment_gateway = models.CharField(max_length=200)
    customer_name = models.ForeignKey(User, on_delete=DO_NOTHING)
    # paid_to = models.ForeignKey(User, on_delete=DO_NOTHING)
    # order = models.ForeignKey("orders.Order", on_delete=CASCADE)
