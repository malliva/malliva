from fastapi import APIRouter, status
from starlette.responses import HTMLResponse, JSONResponse
from config.config_loader import settings

router = APIRouter()

sub_router = APIRouter()


@router.get("/")
async def root():
    """ Root route returns simple guide page
    """
    html_content1 = """
    <a href="/api/v1/docs">/api/v1/docs</a>
    """

    html_content2 = """
    <a href="/maccounts/api/v1/docs">/maccounts/api/v1/docs</a>
    """
    try:
        return HTMLResponse(content=f"{settings.DESCRIPTION} Visit {html_content1} for the platform endpoints, and{html_content2} for the marketplace api endpoints.",
                            status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content=e, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get('/info')
async def info():
    return {
        "app_name": settings.PROJECT_NAME,
        "debug": settings.DEBUG,
        "allowed_image_types": settings.ALLOWED_IMAGE_TYPES,
        "allowed_file_types": settings.ALLOWED_FILE_TYPES,
    }


@sub_router.get("/sub")
def read_sub():
    return {"message": "Hello World from " + settings.ACCOUNT_PROJECT_NAME}
