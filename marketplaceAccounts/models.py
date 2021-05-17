# Marketplace accounts created on the platform, they have users and settings and databases

import uuid
from django.db import models


class MarketplaceAccount(models.Model):

    marketplace_id = models.UUIDField(primary_key=True, default=uuid.uuid4().hex)

    # make it foreign key to marketplace settings
    marketplace_name = models.CharField(max_length=200)

    marketplace_admin = models.ForeignKey("mallivaUsers.User", on_delete=models.CASCADE)
    marketplace_plan_id = models.CharField(max_length=200, default="trial")

    database_name = models.CharField(max_length=200, unique=True)
    subdomain = models.CharField(max_length=200, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
