"""
Settings for malliva project
"""

# from config.locale.alllanguages import LANGUAGE_OPTIONS, LANGUAGE_BIDI_OPTIONS

import logging
from pydantic.types import DirectoryPath
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, validator
from typing import Any, Dict, List, Optional, Union
from pathlib import Path
import os
import secrets
from .global_settings import Settings

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# remember to set global configs


class Settings(Settings):

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
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        'http://malliva.com', 'http://localhost:4200']
    BACKEND_CORS_ORIGINS_REGEX: List = [
        '*.malliva\.com', '*\.localhost']

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # remember to deactivate in production
    OPENAPI_URL: str = "/openapi.json"  # ""

    DEBUG: bool = True

    @validator("EMAILS_FROM_NAME")
    def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            return values["PROJECT_NAME"]
        return v

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "/email-templates/build"
    EMAILS_ENABLED: bool = False

    @validator("EMAILS_ENABLED", pre=True)
    def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
            and values.get("EMAILS_FROM_EMAIL")
        )

    LOG_LEVEL: int = logging.INFO


settings = Settings()