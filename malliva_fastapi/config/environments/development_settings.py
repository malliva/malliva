"""
Settings for malliva project
"""

from pathlib import Path
import os
# from config.locale.alllanguages import LANGUAGE_OPTIONS, LANGUAGE_BIDI_OPTIONS

from pydantic import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Malliva Marketplace Platform"

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY: str = "dont forget to add a secret key here"

    DEBUG: bool = True

    DB_USERNAME: str = "mallivay21"
    DB_PASSWORD: str = "P123Malliva"
    PLATFORM_DB: str = "malliva21_db"
    PLATFORM_DB_HOST: str = "localhost"

    ALLOWED_IMAGE_TYPES: list = ['gif', 'jpg', 'png']

    ALLOWED_FILE_TYPES: list = ['pdf', 'doc', 'docx', 'gif', 'jpg', 'png']
