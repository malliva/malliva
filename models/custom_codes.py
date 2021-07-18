from mongoengine import Document, fields

# Create your fields here.


class CustomCode(Document):
    id = fields.SequenceField(primary_key=True)
    javascript = fields.StringField(max_length=1000, default="")
    css_styles = fields.StringField(max_length=1000, default="")
