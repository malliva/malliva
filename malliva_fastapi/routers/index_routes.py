from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Malliva Marketplace Platform!"}


@router.get('/info/')
async def info():
    return {
        "app_name": settings.APP_NAME,
        "debug": settings.DEBUG,
        "allowed_image_types": settings.ALLOWED_IMAGE_TYPES,
        "allowed_file_types": settings.ALLOWED_FILE_TYPES,
    }
