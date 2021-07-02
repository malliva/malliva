from fastapi import APIRouter
from config.config_loader import settings

router = APIRouter()


@router.get("/")
async def root():
    return {"message": settings.PROJECT_NAME}


@router.get('/info/')
async def info():
    return {
        "app_name": settings.PROJECT_NAME,
        "debug": settings.DEBUG,
        "allowed_image_types": settings.ALLOWED_IMAGE_TYPES,
        "allowed_file_types": settings.ALLOWED_FILE_TYPES,
    }
