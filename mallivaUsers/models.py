# User authentication abstraction for all kinds of users

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    user_context = models.CharField(max_length=200)
    role = models.CharField(max_length=200, default="")
    marketplace = models.ForeignKey(
        "marketplaceAccounts.MarketplaceAccount", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["user_context"]

    # connect to database based on context
    # meta = {'db_alias': 'user-db-alias'}
