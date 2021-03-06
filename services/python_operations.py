import json
from schema.malliva_users import User
import os
import shutil
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from config.config_loader import settings


def convert_mongo_result_to_dict(data):
    """
    convert mongo result to from string json to dict json
    """
    converted_data = json.loads(data.to_json())

    if converted_data["created_at"]:
        # created_at = converted_data.pop("created_at")
        converted_data["created_at"] = format_mongodate(data.created_at)

    if converted_data["updated_at"]:
        # updated_at = converted_data.pop("updated_at")
        converted_data["updated_at"] = format_mongodate(data.updated_at)

    return converted_data


def loop_through_queryset(Model, queryset):
    """
    Handle formating for querysets
    """

    converted_data = json.loads(queryset.to_json())
    print(Model)

    i = 0
    while i < queryset.count():
        converted_data[i] = convert_mongo_result_to_dict(queryset[i])
        converted_data[i] = jsonable_encoder(Model(**converted_data[i]))
        i += 1

    return converted_data


def format_mongodate(date_data):
    """
    convert mongodate to readable format
    """
    # print(date_data.isoformat())
    # print(date_data.strftime("%d-%m-%Y, %H:%M:%S"))

    return date_data.isoformat()


def upload_file(file, storage_path, allowed_content_type, service):
    """
    This will handle all file uploads for malliva
    TODO: Remember to create thumbnails of images, resize images and restrict maximum size of uploaded file
    """
    if service != "local":
        raise HTTPException(detail="Service is not available yet",
                            status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    if file.content_type not in allowed_content_type:
        raise HTTPException(detail="File type is not allowed",
                            status_code=status.HTTP_406_NOT_ACCEPTABLE)

    storage_path = os.path.join(settings.MEDIA_UPLOAD_LOCATION, storage_path)

    try:
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)

        with open(os.path.join(storage_path, file.filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return True
    except:
        return False


def get_request_source(request):
    domain = request.base_url.hostname.split(".")[0]
    domain = domain.split(":")[0]
    return domain
