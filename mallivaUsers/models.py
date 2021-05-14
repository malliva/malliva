# User authentication abstraction for all kinds of users

from mongoengine import *

# import the current settings for this mode
from django.conf import settings

class User(Document):
    first_name = StringField(max_length=200)
    last_name = StringField(max_length=200)
    username = StringField(max_length=200, unique=True, required=True)
    password = StringField(max_length=200, required=True)
    email_address = StringField(max_length=200, unique=True, required=True)
    role = StringField(max_length=200, null=True)
