from enum import unique
from typing import Optional
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from pydantic.types import FilePath, SecretStr, constr


class UserLogin(BaseModel):
    email: Optional[EmailStr] = Field(unique=True)
    password: Optional[SecretStr]


class UserRegister(UserLogin):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[constr(to_lower=True)] = Field(
        description="The user username can be gotten from the email or submitted by user")
    terms_of_service_accepted: Optional[bool] = Field(default=False,
                                                      description="Users will not be able to continue after signing up if they do not accept our terms of service")


class UserUpdate(UserRegister):
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_deleted: Optional[bool] = False


class User(UserUpdate):
    profile_picture: Optional[str] = None
