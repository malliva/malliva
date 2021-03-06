from typing import Optional
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from pydantic.types import SecretStr, constr
from datetime import datetime


class UserLogin(BaseModel):
    email: Optional[EmailStr] = Field(unique=True)
    password: Optional[SecretStr]


class UserRegister(UserLogin):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[constr(to_lower=True)]
    terms_of_service_accepted: Optional[bool] = Field(default=False)


class UserUpdate(UserRegister):
    is_active: Optional[bool] = True
    can_post: Optional[bool] = False
    is_superuser: Optional[bool] = False
    is_deleted: Optional[bool] = False


class User(UserUpdate):
    profile_picture: Optional[str] = None
    created_at: Optional[datetime] = None