import json
import jwt
import datetime
from starlette import status
from starlette.responses import JSONResponse
from config.config_loader import settings
from fastapi import HTTPException
from models.mallivaUsers import User
from dbConnectionManager.database_resolver import get_db_name


def generate_access_token(username, subdomain):
    payload = {
        "user_username": username,
        "subdomain": subdomain,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7, minutes=60),
        "iat": datetime.datetime.utcnow(),
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.SESSION_TOKEN_ALGORITHM)


async def authenticate(request):
    """ 
    Check if User is logged in
    """
    try:
        if request.cookies.get("jwt") is not None:
            token = request.cookies.get("jwt")
        else:
            token = json.loads(request.headers.get(
                "Authorization"))["jwt"]

        if token is None:
            raise HTTPException(detail="User needs to login to access this page.",
                                status_code=status.HTTP_401_UNAUTHORIZED)
    except:
        raise HTTPException(detail="User needs to login to access this page.",
                            status_code=status.HTTP_401_UNAUTHORIZED)

    try:
        payload = jwt.decode(
            jwt=token, key=settings.SECRET_KEY, algorithms=settings.SESSION_TOKEN_ALGORITHM)
    except jwt.ExpiredSignatureError:
        raise HTTPException(detail="User session has expired. Please login again",
                            status_code=status.HTTP_401_UNAUTHORIZED)

    await get_db_name(request)

    try:
        user = User.objects.filter(username=payload["user_username"]).first(
        ).switch_db(settings.ACCOUNT_DEFAULT_ALIAS)
    except:
        return HTTPException(detail="User does not exist", status_code=status.HTTP_401_UNAUTHORIZED)

    if user is None or user.is_deleted is True:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found!")

    if user is None or user.is_active is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="This User has been banned, contact the administrator!")

    return (user, None)
