import logging
import os
from pathlib import Path
from pydantic.env_settings import BaseSettings
from pydantic.types import DirectoryPath
from pydantic import EmailStr
from typing import Optional


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):

    PROJECT_NAME: str = "Malliva Marketplace Platform"
    ACCOUNT_PROJECT_NAME: str = "Malliva API Backend for Marketplace Accounts"
    DESCRIPTION: str = "Welcome to the API Backend for Malliva Platform, here are the Available API endpoints you can connect to"
    ACCOUNT_DESCRIPTION: str = "Welcome to the API Backend for Malliva Marketplace Accounts, here are the Available API endpoints you can connect to"

    API_V1_STR: str = "/api/v1"

    # Database auth details

    DB_USERNAME: str = "mallivay21"
    DB_PASSWORD: str = "P123Malliva"
    PLATFORM_DB_PORT: str = "27017"
    PLATFORM_DB_HOST: str = "malliva33y21_db"
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

    EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr = "min45y@malliva.com"
    FIRST_SUPERUSER_PASSWORD: str = "pbkdf2_sha256$180000$RsvlpMaQUfMK$SLL4KY5ispX8aX2qzO8TcOqOPiLPvRF+5300cGVa8iQ="
    USERS_OPEN_REGISTRATION: bool = False

    ALLOWED_IMAGE_TYPES: list = ['image/jpeg', 'image/png', 'image/gif']

    ALLOWED_FILE_TYPES: list = ['application/pdf']

    SESSION_TOKEN_ALGORITHM: str = "HS256"

    PASSWORD_HASHING_ALGORITHM: str = "bcrypt"

    MEDIA_UPLOAD_LOCATION: DirectoryPath = os.path.join(BASE_DIR, "uploads")

    FILE_SERVICE: str = "local"
