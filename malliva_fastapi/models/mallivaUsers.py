from enum import unique
from typing import Optional
from pydantic import BaseModel, Field
from mongoengine import Document, fields
from datetime import datetime

from pydantic.networks import EmailStr
from pydantic.types import FilePath


class User(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: EmailStr = Field(unique=True)
    username: str = Field(
        description="The user username can be gotten from the email or submitted by user")
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_deleted: Optional[bool] = False
    terms_of_service_accepted: bool = Field(default=False,
                                            description="Users will not be able to continue after signing up if they do not accept our terms of service")
    profile_picture: Optional[FilePath] = None

    class User(Document):
        id = fields.SequenceField(primary_key=True)
        first_name = fields.StringField(max_length=200)
        last_name = fields.StringField(max_length=200)
        username = fields.StringField(
            max_length=200, unique=True, required=False)
        password = fields.StringField(max_length=200)
        email = fields.EmailField(max_length=200, unique=True)
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
