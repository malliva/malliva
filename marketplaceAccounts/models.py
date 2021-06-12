# Marketplace accounts created on the platform, they have users and settings and databases

from django.db import models

# from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class MarketplaceAccount(models.Model):

    id = models.BigAutoField(primary_key=True)

    # make it foreign key to marketplace settings
    marketplace_name = models.CharField(max_length=200)

    # Users own marketplace accounts, all marketplace accounts will be deleted when associated accounts are deleted

    marketplace_admin = models.ForeignKey(User, on_delete=models.CASCADE)

    marketplace_plan_id = models.CharField(max_length=200, default="trial")

    database_name = models.CharField(max_length=200, unique=True)
    subdomain = models.CharField(max_length=200, unique=True)
    domain = models.CharField(max_length=200, unique=True, default="")
    usedomain = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
