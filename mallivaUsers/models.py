# User authentication abstraction for all kinds of users

from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from threadlocals.threadlocals import get_request_variable
from translations.models import Translatable
from django.contrib.contenttypes.fields import GenericRelation
from customFields.models import CustomField, CustomFieldItem


# TODO Evaluate: create abstract models to separate marketplace users from malliva admin


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/domain/users/<username>/<filename>
    return "{0}/{1}/{2}/{3}".format(
        get_request_variable("malliva_domain"),
        "users",
        instance.username,
        filename,
    )


class Permission(models.Model):
    name = models.CharField(max_length=200)


class Role(models.Model):
    name = models.CharField(max_length=200)
    permissions = models.ManyToManyField(Permission)


class User(AbstractUser, Translatable):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, editable=False)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    custom_fields = GenericRelation(CustomField)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class TranslatableMeta:

        fields = ["role"]

    @property
    def set_username(self):
        """
        set username from submited email
        """
        self.username = self.email.split("@")[0]
        # return self.username

    def get_fullname(self):
        return self.first_name + "" + self.last_name

    def soft_delete(self):
        """
        soft delete user accounts instead of deleting it.
        """
        self.is_active = False

    def clean(self):
        super(User, self).clean()
        self.username = self.email.split("@")[0]
        self.updated_at = datetime.now()
