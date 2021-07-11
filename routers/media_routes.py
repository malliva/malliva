import os
from fastapi.exceptions import HTTPException
from dbConnectionManager.database_resolver import get_db_name
from fastapi import Request, APIRouter, status, UploadFile, File
from fastapi.params import Path
from fastapi.responses import JSONResponse, FileResponse
import logging
from config.config_loader import settings
from services.python_operations import upload_file
from services.authentication import authenticate

logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/uploadfile", status_code=status.HTTP_201_CREATED)
async def create_upload_file(request: Request, file: UploadFile = File(...)):
    """
    File upload route
    """
    await authenticate(request)

    # await file.write(os.path.join(
    #    settings.MEDIA_UPLOAD_LOCATION, "file", file.filename))

    if not await upload_file(file, os.path.join(settings.MEDIA_UPLOAD_LOCATION, "file"), settings.ALLOWED_IMAGE_TYPES, settings.FILE_SERVICE):
        raise HTTPException(detail="file could not be uploaded",
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return JSONResponse(content="The file " + file.filename + " was uploaded successfully", status_code=status.HTTP_201_CREATED)


@ router.get("/{file_path:path}")
async def read_files(request: Request, file_path: str):
    """read files """
    logging.info(
        "TODO: we may need to allow only authenticated user to access files for security and cost reasons")

    await get_db_name(request)

    try:
        with open(os.path.join(settings.MEDIA_UPLOAD_LOCATION, file_path), "r") as file:
            return FileResponse(path=os.path.join(settings.MEDIA_UPLOAD_LOCATION, file_path))
    except:
        return JSONResponse(content="File does not exist", status_code=status.HTTP_404_NOT_FOUND)
