# User authentication abstraction for all kinds of users

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from threadlocals.threadlocals import get_request_variable

# TODO Evaluate: create abstract models to separate marketplace users from malliva admin


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/domain/<username>/<filename>
    return "{0}/{1}/{2}".format(
        get_request_variable("malliva_domain"), instance.username, filename
    )


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    user_context = models.CharField(max_length=200)
    role = models.CharField(max_length=200, default="")
    profile_picture = models.ImageField(upload_to=user_directory_path, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username", "user_context"]

    @property
    def set_username(self):
        """
        set username from submited email
        """
        self.username = self.email.split("@")[0]
        # return self.username

    def get_fullname(self):
        return self.first_name + "" + self.last_name
