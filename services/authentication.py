import jwt
import datetime
from starlette import status

from starlette.responses import JSONResponse
from config.config_loader import settings
from fastapi import HTTPException
from models.mallivaUsers import User
from dbConnectionManager.database_resolver import get_db_name


async def generate_access_token(user, subdomain):
    payload = {
        "user_username": user,
        "subdomain": subdomain,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow(),
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.SESSION_TOKEN_ALGORITHM)


async def authenticate(request):

    token = request.cookies.get("jwt")

    if not token:
        return None

    payload = jwt.decode(
        jwt=token, key=settings.SECRET_KEY, algorithms=settings.SESSION_TOKEN_ALGORITHM)

    await get_db_name(request)

    try:
        user = User.objects.filter(username=payload["user_username"]).first(
        ).switch_db(settings.ACCOUNT_DEFAULT_ALIAS)
    except:
        return JSONResponse(content="User does not exist", status_code=status.HTTP_400_BAD_REQUEST)

    if user is None or user.is_deleted is True:
        raise HTTPException(status_code=400, detail="User not found!")

    if user is None or user.is_active is False:
        raise HTTPException(
            status_code=400, detail="This User has been banned, contact the administrator!")

    return (user, None)
