# Marketplace accounts created on the platform, they have users and settings and databases

from django.db import models

# from django.conf import settings
from django.contrib.auth import get_user_model
from settingsManager.models import Configuration

User = get_user_model()


class Plan(models.Model):
    id = models.BigAutoField(primary_key=True)
    plan_name = models.CharField(max_length=200)
    features = models.CharField(max_length=1000, default="")


class Subscription(models.Model):
    id = models.BigAutoField(primary_key=True)
    current_plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
    last_subscription_date = models.DateTimeField()
    expiration_date = models.DateTimeField()


class MarketplaceAccount(models.Model):

    id = models.BigAutoField(primary_key=True)
    marketplace_name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="1")
    database_name = models.CharField(max_length=200, unique=True)
    subdomain = models.CharField(max_length=200, unique=True)
    domain = models.CharField(max_length=200, unique=True, default="")
    use_domain = models.BooleanField(default=False)
    configuration = models.ForeignKey(
        Configuration, on_delete=models.SET_DEFAULT, default="1"
    )
    subscription = models.ForeignKey(
        Subscription, on_delete=models.SET_DEFAULT, default="1"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
