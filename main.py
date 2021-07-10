from fastapi import FastAPI
import jwt
from mongoengine.connection import disconnect_all
from starlette.middleware.cors import CORSMiddleware
from config.config_loader import settings
from dbConnectionManager.db_session import platform_db_connection_instance, accounts_db_connection_instance
from routers.all_routes import malliva_routers, sub_malliva_routers
from routers import index_routes, sitewide_seo

# initialize FastAPI

malliva_api = FastAPI(title=settings.PROJECT_NAME,  # root_path=settings.API_V1_STR,
                      description=settings.DESCRIPTION,
                      openapi_url=f"{settings.API_V1_STR + settings.OPENAPI_URL}",
                      docs_url=f"{settings.API_V1_STR}/docs",
                      version="1.0")

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    malliva_api.add_middleware(
        CORSMiddleware,
        # allow_origin_regex=settings.BACKEND_CORS_ORIGINS_REGEX,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=['jwt', 'Origin', 'Access-Control-Request-Method'])

malliva_api.middleware("http")


@ malliva_api.on_event("startup")
async def startup():
    print("start up tasks running")
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
