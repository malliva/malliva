import uuid
from django.db import models
from django.db.models.fields import UUIDField

# Create your models here.


class MarketplaceRouter(models.Model):

    marketplace_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    marketplace_name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    marketplace_domain = models.CharField(max_length=200)
    use_domain = models.BooleanField(default=False)
    marketplace_version = models.CharField(max_length=200)
    account_id = models.ForeignKey("mallivaUsers.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    @property
    def database_name(self):
        return self.identity + self.pk
