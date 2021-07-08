from datetime import datetime
from mongoengine import Document, fields


class User(Document):
    id = fields.SequenceField(primary_key=True)
    first_name = fields.StringField(max_length=200)
    last_name = fields.StringField(max_length=200)
    username = fields.StringField(
        max_length=200, unique=True, required=True)
    password = fields.StringField(max_length=200, required=True)
    email = fields.EmailField(max_length=200, unique=True, required=True)
    is_active = fields.BooleanField(default=True)
    is_superuser = fields.BooleanField(default=False)
    is_deleted = fields.BooleanField(default=False)
    terms_of_service_accepted = fields.BooleanField(default=False)
    profile_picture = fields.StringField(required=False)
    created_at = fields.DateTimeField(default=datetime.utcnow())
    updated_at = fields.DateTimeField(default=datetime.utcnow())

    def __str__(self):
        # return description of field
        return self.get_fullname()

    @property
    def set_username(self):
        """
        set username from submited email
        """
        self.username = self.email.split("@")[0]

    def get_fullname(self):
        return self.first_name + " " + self.last_name

    def soft_delete(self):
        """
        soft delete user accounts instead of deleting it.
        """
        self.is_deleted = True
