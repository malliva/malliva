import os

from fastapi.param_functions import Body, Depends
from services.python_operations import upload_file
from fastapi import APIRouter, Request, status, HTTPException, File, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic.types import constr
from schema.mallivaUsers import User, UserRegister, UserUpdate
from models.mallivaUsers import User as UserModel
from dbConnectionManager.database_resolver import get_db_name
from dbConnectionManager.db_session import accounts_db_connection_instance
from config.config_loader import settings
from services.python_operations import convert_mongo_result_to_dict, loop_through_queryset
from security.authentication import get_password_hash
from services.authentication import authenticate

router = APIRouter()


@router.post("/", response_model=User)
async def create_user(user: UserRegister, request: Request):

    # User doesn't need to login to signup
    # current_user = await authenticate(request)
    await get_db_name(request)

    user_data = jsonable_encoder(user)

    try:
        user_data["password"] = await get_password_hash(user.password.get_secret_value())
    except:
        HTTPException(detail="Password field is required!",
                      status_code=status.HTTP_404_NOT_FOUND)

    try:
        instance = UserModel(
            **user_data).switch_db(settings.ACCOUNT_DEFAULT_ALIAS)
    except:
        raise HTTPException(detail="Marketplace database does not exist, please use the right marketplace address.",
                            status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    try:
        instance.save()
        instance = await convert_mongo_result_to_dict(instance)
        instance = jsonable_encoder(User(**instance))
        await accounts_db_connection_instance.end_db_connection()
        return JSONResponse(content=instance, status_code=status.HTTP_201_CREATED)
    except:
        raise HTTPException(detail="User account for " + user_data["first_name"] + " could not be created. Check required fields, Email or Username already exists.",
                            status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.get("/me", tags=["users"])
async def read_user_me(request: Request):
    current_user = await authenticate(request)

    try:
        current_user = await convert_mongo_result_to_dict(current_user[0])
        current_user = jsonable_encoder(User(**current_user))
        await accounts_db_connection_instance.end_db_connection()
        return JSONResponse(content=current_user, status_code=status.HTTP_302_FOUND)
    except:
        raise HTTPException(detail="This user could not be found",
                            status_code=status.HTTP_404_NOT_FOUND)


@router.get("/{username}", response_model=User)
async def read_user(username: constr(to_lower=True), request: Request):

    await get_db_name(request)

    try:
        instance = UserModel.objects.filter(username=username).first().switch_db(
            settings.ACCOUNT_DEFAULT_ALIAS)
    except:
        raise HTTPException(detail="Marketplace database does not exist, please use the right marketplace address.",
                            status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    try:
        instance = await convert_mongo_result_to_dict(instance)
        instance = jsonable_encoder(User(**instance))
        await accounts_db_connection_instance.end_db_connection()
        return JSONResponse(content=instance, status_code=status.HTTP_302_FOUND)
    except:
        raise HTTPException(detail="User with username: " + username + " could not be found",
                            status_code=status.HTTP_404_NOT_FOUND)

# List all Users in the database


@ router.get("/", response_model=User)
async def read_users(request: Request):
    """
    Retrieve users.
    """

    current_user = await authenticate(request)

    try:
        queryset = UserModel.objects.all().using(
            settings.ACCOUNT_DEFAULT_ALIAS)
        queryset = await loop_through_queryset(queryset)
        await accounts_db_connection_instance.end_db_connection()
        return JSONResponse(content=queryset, status_code=status.HTTP_302_FOUND)
    except:
        raise HTTPException(detail="No user found",
                            status_code=status.HTTP_404_NOT_FOUND)


@ router.put("/me", response_model=User)
async def update_user_me(request: Request, user: UserUpdate, file: UploadFile = File(None)):

    current_user = await authenticate(request)

    update_data = user.dict(exclude_unset=True)
    update_data = jsonable_encoder(update_data)

    if "password" in update_data:
        update_data["password"] = get_password_hash(
            user.password.get_secret_value())

    marketplace_domain = request.base_url.hostname.split(".")[0]
    upload_path = os.path.join(
        settings.MEDIA_UPLOAD_LOCATION, marketplace_domain, "users", current_user.id)
    if "profile_picture" in update_data:
        if not await upload_file(file, upload_path, settings.ALLOWED_IMAGE_TYPES, settings.FILE_SERVICE):
            raise HTTPException(detail="file could not be uploaded",
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        update_data["profile_picture"] = upload_path

    try:
        current_user[0].update(**update_data)
        updated_instance = UserModel.objects.filter(
            **update_data).first().switch_db(settings.ACCOUNT_DEFAULT_ALIAS)
        updated_instance = await convert_mongo_result_to_dict(updated_instance)
        updated_instance = jsonable_encoder(User(**updated_instance))
        await accounts_db_connection_instance.end_db_connection()
        return JSONResponse(content=updated_instance, status_code=status.HTTP_206_PARTIAL_CONTENT)
    except:
        raise HTTPException(detail="User account for " + current_user[0].username + " could not be updated.",
                            status_code=status.HTTP_304_NOT_MODIFIED)


@ router.put("/{usernam}", response_model=User)
async def update_user(request: Request, usernam: constr(to_lower=True), user: UserUpdate = Depends(), profile_picture: UploadFile = File(None)):

    await get_db_name(request)

    update_data = user.dict(exclude_unset=True)
    print(update_data)
    update_data = jsonable_encoder(update_data)

    if "password" in update_data:
        update_data["password"] = get_password_hash(
            user.password.get_secret_value())

    try:
        instance = UserModel.objects.filter(
            username=usernam).first().switch_db(settings.ACCOUNT_DEFAULT_ALIAS)

        marketplace_domain = request.base_url.hostname.split(".")[0]
        upload_path = os.path.join(
            settings.MEDIA_UPLOAD_LOCATION, marketplace_domain, "users", instance.id)
        print("hello here")
        if "profile_picture" in update_data:
            if not await upload_file(profile_picture, upload_path, settings.ALLOWED_IMAGE_TYPES, settings.FILE_SERVICE):
                raise HTTPException(detail="file could not be uploaded",
                                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

            update_data["profile_picture"] = upload_path

        instance.update(**update_data)
        updated_instance = UserModel.objects.filter(
            **update_data).first().switch_db(settings.ACCOUNT_DEFAULT_ALIAS)
        updated_instance = await convert_mongo_result_to_dict(updated_instance)
        updated_instance = jsonable_encoder(User(**updated_instance))
        await accounts_db_connection_instance.end_db_connection()
        return JSONResponse(content=updated_instance, status_code=status.HTTP_206_PARTIAL_CONTENT)
    except:
        raise HTTPException(detail="User account for " + username + " could not be updated.",
                            status_code=status.HTTP_304_NOT_MODIFIED)


# delete personal user
@ router.delete("/me")
async def delete_user_me(request: Request):
    current_user = await authenticate(request)

    try:
        current_user[0].delete()
        return JSONResponse(content="The User with username: " + current_user[0].username + " was deleted successfully", status_code=status.HTTP_410_GONE)
    except:
        raise HTTPException(detail="Your user account could not be deleted.",
                            status_code=status.HTTP_400_BAD_REQUEST)


# delete only one user
@ router.delete("/{username}")
async def delete_user(username: constr(to_lower=True), request: Request):

    current_user = await authenticate(request)

    try:
        instance = UserModel.objects.filter(
            username=username).first().switch_db(settings.ACCOUNT_DEFAULT_ALIAS)
        instance.delete()
        await accounts_db_connection_instance.end_db_connection()
        return JSONResponse(content="The User with username: " + username + " was deleted successfully", status_code=status.HTTP_410_GONE)
    except:
        raise HTTPException(detail="User account for " + username + " could not be deleted.",
                            status_code=status.HTTP_400_BAD_REQUEST)


# delete selected users
@ router.delete("/")
async def delete_users(request: Request):
    current_user = await authenticate(request)
    return JSONResponse(content="This route has not been setup yet, check back later", status_code=status.HTTP_306_RESERVED)
