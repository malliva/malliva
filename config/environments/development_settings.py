"""
Settings for malliva project
"""

# from config.locale.alllanguages import LANGUAGE_OPTIONS, LANGUAGE_BIDI_OPTIONS

import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, validator


class Settings(BaseSettings):

    PROJECT_NAME: str = "Malliva Marketplace Platform"
    ACCOUNT_PROJECT_NAME: str = "Malliva API Backend for Marketplace Accounts"
    DESCRIPTION: str = "Welcome to the API Backend for Malliva Platform, here are the Available API endpoints you can connect to"
    ACCOUNT_DESCRIPTION: str = "Welcome to the API Backend for Malliva Marketplace Accounts, here are the Available API endpoints you can connect to"

    API_V1_STR: str = "/api/v1"

    MALLIVA_DOMAIN: list = ["localhost:8000", "localhost",
                            "127.0.0.1", "127.0.0.1:8000", "malliva.com",
                            "malliva.com:8000", "www.malliva.com", "www.malliva.com:8000"]

    # remember to make this static in production

    # SECRET_KEY: str = secrets.token_urlsafe(32)
    SECRET_KEY: str = "-MmPYkSksyccaQA7fSCNVVHTdFr41IGm3qD70YARmLg"

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: Optional[str]
    SERVER_HOST: Optional[AnyHttpUrl]
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # Database auth details

    DB_USERNAME: str = "mallivay21"
    DB_PASSWORD: str = "P123Malliva"
    PLATFORM_DB_PORT: str = "27017"
    PLATFORM_DB_HOST: str = "localhost"
    PLATFORM_DEFAULT_DB: str = "malliva21_db"
    PLATFORM_DEFAULT_ALIAS: str = "default"

    ACCOUNT_DEFAULT_ALIAS: str = "mAlLiVa21YcLiEnT"

    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    # remember to deactivate in production
    OPENAPI_URL: str = "/openapi.json"  # ""

    DEBUG: bool = True

    @validator("EMAILS_FROM_NAME")
    def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            return values["PROJECT_NAME"]
        return v

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "/app/app/email-templates/build"
    EMAILS_ENABLED: bool = False

    @validator("EMAILS_ENABLED", pre=True)
    def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
            and values.get("EMAILS_FROM_EMAIL")
        )

    EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr = "min45y@malliva.com"
    FIRST_SUPERUSER_PASSWORD: str = "pbkdf2_sha256$180000$RsvlpMaQUfMK$SLL4KY5ispX8aX2qzO8TcOqOPiLPvRF+5300cGVa8iQ="
    USERS_OPEN_REGISTRATION: bool = False

    ALLOWED_IMAGE_TYPES: list = ['gif', 'jpg', 'png']

    ALLOWED_FILE_TYPES: list = ['pdf', 'doc', 'docx', 'gif', 'jpg', 'png']

    SESSION_TOKEN_ALGORITHM: str = "HS256"

    PASSWORD_HASHING_ALGORITHM: str = "bcrypt"


settings = Settings()
