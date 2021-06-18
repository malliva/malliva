# Marketplace accounts created on the platform, they have users and settings and databases

from django.db import models
from datetime import timedelta

# from django.conf import settings
from django.contrib.auth import get_user_model
from settingsManager.models import Configuration

User = get_user_model()


class Plan(models.Model):
    id = models.BigAutoField(primary_key=True)
    plan_name = models.CharField(max_length=200)
    features = models.CharField(max_length=1000, default="")
    duration = models.DurationField()
    price = models.FloatField(default="00.0")
    user_limit = models.IntegerField(default="100")


class Subscription(models.Model):
    id = models.BigAutoField(primary_key=True)
    current_plan = models.OneToOneField(Plan, on_delete=models.CASCADE, null=True)
    first_subscription_date = models.DateTimeField()
    last_subscription_date = models.DateTimeField()
    next_expiration_date = models.DateTimeField()


class MarketplaceAccount(models.Model):

    id = models.BigAutoField(primary_key=True)
    marketplace_name = models.CharField(max_length=200)
    owner = models.OneToOneField(User, on_delete=models.SET_DEFAULT, default="1")
    database_name = models.CharField(max_length=200, unique=True, editable=False)
    subdomain = models.CharField(max_length=200, unique=True, editable=False)
    domain = models.CharField(max_length=200, unique=True, default="")
    use_domain = models.BooleanField(default=False)
    configuration = models.OneToOneField(
        Configuration, on_delete=models.SET_DEFAULT, default="1"
    )
    subscription = models.OneToOneField(
        Subscription, on_delete=models.SET_DEFAULT, default="1"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
