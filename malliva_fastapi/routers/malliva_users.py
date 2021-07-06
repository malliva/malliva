import re
from fastapi import APIRouter, Request, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schema.mallivaUsers import User
from models.mallivaUsers import User as UserModel
from dbConnectionManager.database_resolver import get_db_name
from dbConnectionManager.db_session import platform_db_connection_instance, accounts_db_connection_instance
from config.config_loader import settings
from services.python_operations import convert_mongo_result_to_dict, loop_through_queryset

router = APIRouter()


@router.post("/", response_model=User)
async def create_user(user: User, request: Request):

    current_db = await get_db_name(request)

    user = jsonable_encoder(user)

    # resolve domain from db
    try:
        await accounts_db_connection_instance.register_new_db_connection(current_db=current_db)
    except:
        raise HTTPException(detail="Could not connect to database",
                            status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    instance = UserModel(**user).switch_db(settings.ACCOUNT_DEFAULT_ALIAS)

    try:
        instance.save()
        return JSONResponse(content=user, status_code=status.HTTP_201_CREATED)
    except:
        raise HTTPException(detail="User account for " + user["first_name"] + " could not be created. Email or Username already exists.",
                            status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.get("/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/{username}", response_model=User)
async def read_user(username: str, request: Request):

    current_db = await get_db_name(request)

    # resolve domain from db
    try:
        await accounts_db_connection_instance.register_new_db_connection(current_db=current_db)
    except:
        raise HTTPException(detail="Could not connect to database",
                            status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    try:
        instance = UserModel.objects.filter(username=username).first().switch_db(
            settings.ACCOUNT_DEFAULT_ALIAS)
        instance = await convert_mongo_result_to_dict(instance)
        return JSONResponse(content=instance, status_code=status.HTTP_302_FOUND)
    except:
        raise HTTPException(detail="User with username " + username + " could not be found",
                            status_code=status.HTTP_404_NOT_FOUND)

# List all Users in the database


@ router.get("/", response_model=User)
async def read_users(request: Request):
    """
    Retrieve users.
    """

    current_db = await get_db_name(request)

    # resolve domain from db
    try:
        await accounts_db_connection_instance.register_new_db_connection(current_db=current_db)
    except:
        raise HTTPException(detail="Could not connect to database",
                            status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    try:
        queryset = UserModel.objects.all().using(
            settings.ACCOUNT_DEFAULT_ALIAS)
        queryset = await loop_through_queryset(queryset)
        return JSONResponse(content=queryset, status_code=status.HTTP_302_FOUND)
    except:
        raise HTTPException(detail="No user found",
                            status_code=status.HTTP_404_NOT_FOUND)


@ router.put("/me")
async def update_user_me():
    return [{"username": "Rick"}, {"username": "Morty"}]


@ router.put("/{username}")
async def update_user():
    return [{"username": "Rick"}, {"username": "Morty"}]


# delete personal user
@ router.delete("/me")
async def delete_user_me():
    return [{"username": "Rick"}, {"username": "Morty"}]


# delete only one user
@ router.delete("/{username}")
async def delete_user():
    return [{"username": "Rick"}, {"username": "Morty"}]


# delete selected users
@ router.delete("/")
async def delete_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
