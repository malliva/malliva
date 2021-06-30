from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from config.config_loader import settings
from dbConnectionManager.tenant_connections import connect_to_database
from routers.all_routes import malliva_routers
from routers import index_routes

# initialize FastAPI

malliva_api = FastAPI(title=settings.PROJECT_NAME,
                      description="Welcome to the API Backend for Malliva Platform, here are the Available API endpoints you can connect to",
                      version="1.0", openapi_url=f"{settings.API_V1_STR}/openapi.json")

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    malliva_api.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

malliva_api.include_router(
    index_routes.router, tags=["index"])

malliva_api.include_router(malliva_routers, prefix=settings.API_V1_STR)

# malliva_routers.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )
