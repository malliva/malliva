from fastapi import FastAPI
from mongoengine.connection import disconnect_all
from starlette.middleware.cors import CORSMiddleware
from config.config_loader import settings
from dbConnectionManager.db_session import platform_db_connection_instance, accounts_db_connection_instance
from routers.all_routes import malliva_routers, sub_malliva_routers
import logging

logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)

# initialize FastAPI

malliva_api = FastAPI(title=settings.PROJECT_NAME,  # root_path=settings.API_V1_STR,
                      description=settings.DESCRIPTION,
                      openapi_url=f"{settings.API_V1_STR + settings.OPENAPI_URL}",
                      docs_url=f"{settings.API_V1_STR}/docs",
                      version="1.0")

# Set all CORS enabled origins
origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:8000",
    "http://localhost:8080",
]

malliva_api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@ malliva_api.on_event("startup")
async def startup():
    logger.info("start up tasks running")
    # initiallize database connection settings
    await platform_db_connection_instance.initiate_db_connection()
    await accounts_db_connection_instance.initiate_db_connection()


@ malliva_api.on_event("shutdown")
async def shutdown():
    disconnect_all()


# import other routes
malliva_api.include_router(malliva_routers, prefix=settings.API_V1_STR)

# malliva_routers.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )

# ___________________________________________________________________________

sub_malliva_api = FastAPI(title=settings.ACCOUNT_PROJECT_NAME,
                          description=settings.ACCOUNT_DESCRIPTION,  # root_path=settings.API_V1_STR,
                          openapi_url=f"{settings.API_V1_STR + settings.OPENAPI_URL}",
                          docs_url=f"{settings.API_V1_STR}/docs",
                          version="1.0")


sub_malliva_api.include_router(sub_malliva_routers, prefix=settings.API_V1_STR)


malliva_api.mount("/maccounts", sub_malliva_api)
