import jwt
import datetime
from config.config_loader import settings
from fastapi import HTTPException
from models.mallivaUsers import User


def generate_access_token(user, subdomain):
    payload = {
        "user_username": user,
        "subdomain": subdomain,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow(),
    }

    print(settings.SECRET_KEY)

    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def authenticate(request):

    token = request.COOKIES.get("jwt")

    if not token:
        return None

    payload = jwt.decode(
        jwt=token, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM)

    user = User.objects.filter(username=payload["user_username"]).first()
    user = payload["user_username"]

    # find subdomain in db

    subdomain = payload["subdomain"]

    if user is None or user.is_deleted is True:
        raise HTTPException(status_code=400, detail="User not found!")

    if user is None or user.is_active is False:
        raise HTTPException(status_code=400, detail="User has been banned!")

    return (user, None)
