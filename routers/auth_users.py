from fastapi import APIRouter, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.requests import Request
from schema.mallivaUsers import User, UserLogin
from models.mallivaUsers import User as UserModel
from services.authentication import generate_access_token, authenticate
from security.authentication import verify_password, get_password_hash
from dbConnectionManager.database_resolver import get_db_name
from dbConnectionManager.db_session import accounts_db_connection_instance
from services.python_operations import convert_mongo_result_to_dict
from config.config_loader import settings

router = APIRouter()


@router.post('/login', response_model=UserLogin)
async def authenticate_user(request: Request, user: UserLogin):
    await get_db_name(request)

    user_data = user.dict(exclude_unset=True)

    try:
        instance = UserModel.objects.filter(
            email=user_data["email"]).first().switch_db(settings.ACCOUNT_DEFAULT_ALIAS)

        instance = await convert_mongo_result_to_dict(instance)

        if await verify_password(user.password.get_secret_value(), instance["password"]):
            token = await generate_access_token(instance["username"], request.base_url.hostname.split(".")[0])

            instance = jsonable_encoder(User(**instance))
            response = JSONResponse(
                content=instance, status_code=status.HTTP_202_ACCEPTED)
            response.set_cookie(key="jwt", value=token, httponly=True)

            await accounts_db_connection_instance.end_db_connection()
            return response
        else:
            print("here i am")
            raise HTTPException(detail="User cannot login. Email or password not correct.",
                                status_code=status.HTTP_400_BAD_REQUEST)
    except:
        raise HTTPException(detail="User cannot login. Email or password not correct.",
                            status_code=status.HTTP_400_BAD_REQUEST)


@router.post('/logout')
async def signout_user():

    response = JSONResponse(
        content="User logged out successfully", status_code=status.HTTP_202_ACCEPTED)
    response.delete_cookie(key="jwt")

    return response
