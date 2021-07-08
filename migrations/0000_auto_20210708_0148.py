from mongoengine_migrate.actions import *
import pymongo

# Existing data processing policy
# Possible values are: strict, relaxed
policy = "strict"

# Names of migrations which the current one is dependent by
dependencies = [
]

# Action chain
actions = [
    CreateDocument('User', collection='user'),
    CreateField('User', 'is_active', choices=None, db_field='is_active', default=True,
        null=False, primary_key=False, required=False, sparse=False, type_key='BooleanField',
        unique=False, unique_with=None),
    CreateField('User', 'first_name', choices=None, db_field='first_name', default=None,
        max_length=200, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('User', 'is_superuser', choices=None, db_field='is_superuser',
        default=False, null=False, primary_key=False, required=False, sparse=False,
        type_key='BooleanField', unique=False, unique_with=None),
    CreateField('User', 'is_deleted', choices=None, db_field='is_deleted', default=False,
        null=False, primary_key=False, required=False, sparse=False, type_key='BooleanField',
        unique=False, unique_with=None),
    CreateField('User', 'password', choices=None, db_field='password', default=None,
        max_length=200, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('User', 'created_at', choices=None, db_field='created_at', default=None,
        null=False, primary_key=False, required=False, sparse=False, type_key='DateTimeField',
        unique=False, unique_with=None),
    CreateField('User', 'last_name', choices=None, db_field='last_name', default=None,
        max_length=200, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('User', 'updated_at', choices=None, db_field='updated_at', default=None,
        null=False, primary_key=False, required=False, sparse=False, type_key='DateTimeField',
        unique=False, unique_with=None),
    CreateField('User', 'profile_picture', choices=None, db_field='profile_picture',
        default=None, max_length=None, min_length=None, null=False, primary_key=False,
        regex=None, required=False, sparse=False, type_key='StringField', unique=False,
        unique_with=None),
    CreateField('User', 'email', allow_ip_domain=False, allow_utf8_user=False, choices=None,
        db_field='email', default=None, domain_whitelist=[], max_length=200, min_length=None,
        null=False, primary_key=False, regex=None, required=True, sparse=False,
        type_key='EmailField', unique=True, unique_with=None),
    CreateField('User', 'username', choices=None, db_field='username', default=None,
        max_length=200, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=True, unique_with=None),
    CreateField('User', 'terms_of_service_accepted', choices=None,
        db_field='terms_of_service_accepted', default=False, null=False, primary_key=False,
        required=False, sparse=False, type_key='BooleanField', unique=False, unique_with=None),
    CreateIndex('User', 'email_1', fields=[('email', pymongo.ASCENDING)], sparse=False,
        unique=True),
    CreateIndex('User', 'username_1', fields=[('username', pymongo.ASCENDING)],
        sparse=False, unique=True),
]