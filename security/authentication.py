from re import I
from passlib.context import CryptContext
from config.config_loader import settings

pwd_context = CryptContext(
    schemes=[settings.PASSWORD_HASHING_ALGORITHM], deprecated="auto")


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
