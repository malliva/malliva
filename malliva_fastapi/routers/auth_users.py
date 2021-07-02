from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from starlette.requests import Request
from models.mallivaUsers import User
from services.authentication import generate_access_token, authenticate
from security.authentication import verify_password, get_password_hash

router = APIRouter()


@router.post('/login')
async def authenticate_user(request: Request):
    return {"message": "We will authenticate users here"}


@router.post('/logout')
async def signout_user():
    return {"message": "We will authenticate users here"}
