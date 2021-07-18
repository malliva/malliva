# Marketplace accounts created on the platform, they have users and settings and databases

from datetime import timedelta, datetime
from enum import Enum
from mongoengine.queryset.base import DO_NOTHING
from .malliva_users import User as UserModel
from mongoengine import Document, EmbeddedDocument, fields


class Plan(Document):
    id = fields.SequenceField(primary_key=True)
    plan_name = fields.StringField(max_length=50, required=True)
    features = fields.DynamicField(default={})
    duration = fields.IntField(required=True)
    price = fields.FloatField(default="00.0")

    meta = {'db_alias': 'default'}


class Subscription(Document):
    id = fields.SequenceField(primary_key=True)
    current_plan = fields.ReferenceField(
        Plan, required=True, reverse_delete_rule=DO_NOTHING)
    owner = fields.ReferenceField(
        UserModel, required=True, reverse_delete_rule=DO_NOTHING)
    first_subscription_date = fields.DateTimeField(
        required=True, default=datetime.now())
    last_subscription_date = fields.DateTimeField(null=True, default=None)
    next_expiration_date = fields.DateTimeField(
        default=datetime.now() + timedelta(days=30))
    is_active = fields.BooleanField(default=False)

    meta = {'db_alias': 'default'}


class MallivaAccount(Document):

    class MARKETPLACE_MODE(Enum):
        DEVELOPMENT = "DEVELOPMENT"
        PRODUCTION = "PRODUCTION"

    id = fields.SequenceField(primary_key=True)
    marketplace_name = fields.StringField(max_length=200)
    owner = fields.ReferenceField(
        UserModel, reverse_delete_rule=DO_NOTHING, default="1")
    database_name = fields.StringField(max_length=200, default="", unique=True)
    subdomain = fields.StringField(max_length=200, unique=True)
    domain = fields.StringField(max_length=200, unique=True, default="")
    use_domain = fields.BooleanField(default=False)
    # configuration = models.OneToOneField(Configuration, on_delete=models.SET_DEFAULT, default="1")
    curent_mode = fields.EnumField(
        MARKETPLACE_MODE, default=MARKETPLACE_MODE.DEVELOPMENT)
    subscription = fields.ReferenceField(
        Subscription, reverse_delete_rule=DO_NOTHING, default="1")
    created_at = fields.DateTimeField(auto_now_add=True)
    updated_at = fields.DateTimeField(auto_now_add=True)

    meta = {'db_alias': 'default'}
