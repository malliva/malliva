# User authentication abstraction for all kinds of users

from dbConnectionManager.tenant_connections import connect_to_database
from mongoengine import Document, EmbeddedDocument, fields, queryset
from datetime import datetime
from django.conf import settings
from threadlocals.threadlocals import get_request_variable
from django.contrib.auth.hashers import make_password, check_password


# TODO Evaluate: create abstract models to separate marketplace users from malliva admin

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/domain/users/<username>/<filename>
    return "{0}/{1}/{2}/{3}".format(
        get_request_variable("malliva_domain"),
        "users",
        instance.username,
        filename,
    )


class Permission(Document):
    name = fields.StringField(max_length=200)


class Role(Document):
    name = fields.StringField(max_length=200)
    permissions = fields.ReferenceField(Permission)


class User(Document):
    first_name = fields.StringField(max_length=200)
    last_name = fields.StringField(max_length=200)
    username = fields.StringField(max_length=200, unique=True)
    password = fields.StringField(max_length=200)
    email = fields.EmailField(max_length=200, unique=True)
    is_active = fields.BooleanField(default=True)
    is_superuser = fields.BooleanField(default=False)
    is_deleted = fields.BooleanField(default=False)
    terms_of_service_accepted = fields.BooleanField(default=False)
    profile_picture = fields.ImageField(required=False)
    created_at = fields.DateTimeField(default=datetime.utcnow())
    updated_at = fields.DateTimeField(default=datetime.utcnow())

    meta = {"allow_inheritance": True, "strict": False}

    def __str__(self):
        # return description of field
        return self.get_fullname()

    @property
    def set_username(self):
        """
        set username from submited email
        """
        self.username = self.email.split("@")[0]

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """

        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def get_fullname(self):
        return self.first_name + " " + self.last_name

    def soft_delete(self):
        """
        soft delete user accounts instead of deleting it.
        """
        self.is_deleted = True

    def clean(self):
        super(User, self).clean()
        if self.username is None:
            self.username = self.email.split("@")[0]
        self.updated_at = datetime.now()


class MarketplaceUser(User):
    """
    Users stored here will be saved in their respective databases
    """

    meta = {"db_alias": "marketplace_dbs"}
