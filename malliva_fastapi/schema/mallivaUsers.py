from enum import unique
from typing import Optional
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from pydantic.types import FilePath


class User(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: EmailStr = Field(unique=True)
    username: str = Field(
        description="The user username can be gotten from the email or submitted by user")
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_deleted: Optional[bool] = False
    terms_of_service_accepted: bool = Field(default=False,
                                            description="Users will not be able to continue after signing up if they do not accept our terms of service")
    profile_picture: Optional[FilePath] = None
