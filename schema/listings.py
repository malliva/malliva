from enum import unique
from typing import Optional
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from pydantic.types import FilePath, confloat, conlist


class Listing(BaseModel):
    title: str
    price: confloat(lt=100000.0)
    posted_by: str
    category: Optional[int] = 1
    description: str = None
    listing_images: Optional[conlist(FilePath, max_items=5)] = None
    visible: bool = True
