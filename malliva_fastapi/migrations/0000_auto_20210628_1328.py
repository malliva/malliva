from mongoengine_migrate.actions import *

# Existing data processing policy
# Possible values are: strict, relaxed
policy = "strict"

# Names of migrations which the current one is dependent by
dependencies = [
]

# Action chain
actions = [
    CreateDocument('Item', collection='item'),
    CreateField('Item', 'description', choices=None, db_field='description', default=None,
        max_length=400, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('Item', 'tax', choices=None, db_field='tax', default=None, max_value=None,
        min_value=None, null=False, primary_key=False, required=False, sparse=False,
        type_key='FloatField', unique=False, unique_with=None),
    CreateField('Item', 'price', choices=None, db_field='price', default=None,
        max_value=None, min_value=None, null=False, primary_key=False, required=False,
        sparse=False, type_key='FloatField', unique=False, unique_with=None),
    CreateField('Item', 'name', choices=None, db_field='name', default=None, max_length=100,
        min_length=None, null=False, primary_key=False, regex=None, required=False,
        sparse=False, type_key='StringField', unique=False, unique_with=None),
]