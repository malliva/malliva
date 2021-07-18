from enum import Enum
from typing import Any, TypeVar
from pydantic.main import BaseModel


class CustomFieldType(Enum):
    DROPDOWN = "DROPDOWN"
    TEXT = "TEXT"
    NUMBER = "NUMBER"
    LOCATION = "LOCATION"
    DATE = "DATE"
    FILE = "FILE"


class AssociatedModel(Enum):
    USER = "USER"
    LISTING = "LISTING"


class CustomField(BaseModel):
    """
    This will allow users create new custom fields for User or listing models
    """
    field_name: str = None
    field_type: CustomFieldType = None
    is_required: bool = False
    visible: bool = None


class CustomFieldItem(CustomField):
    """
    This will store the content of every created content fields per user or listing
    """
    content: Any = None
