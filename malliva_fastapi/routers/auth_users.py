from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from models.mallivaUsers import User

router = APIRouter()


@router.post('/login')
async def authenticate_user():
    return {"message": "We will authenticate users here"}


@router.post('/logout')
async def signout_user():
    return {"message": "We will authenticate users here"}
