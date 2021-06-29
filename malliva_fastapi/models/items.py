from typing import Optional
from pydantic import BaseModel
from mongoengine import Document, fields


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Item(Document):
        name = fields.StringField(max_length=100)
        description = fields.StringField(max_length=400, required=False)
        price = fields.FloatField()
        tax = fields.FloatField(required=False)
