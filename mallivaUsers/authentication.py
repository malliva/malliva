# This will handle user authentications, cookies, and sessions

import jwt
import datetime
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.contrib.auth import get_user_model


def generate_access_token(user):
    payload = {
        "user_username": user.username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow(),
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


class jwtAuthentication(BaseAuthentication):
    def authenticate(self, request):

        token = request.COOKIES.get("jwt")

        if not token:
            return None

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except:
            raise exceptions.AuthenticationFailed("unauthenticated")

        user = (
            get_user_model().objects.filter(username=payload["user_username"]).first()
        )

        if user is None or user.is_active is False:
            raise exceptions.AuthenticationFailed("User not found")

        return (user, None)
