from fastapi import APIRouter
from routers import malliva_users
from routers import auth_users

malliva_routers = APIRouter()


malliva_routers.include_router(
    auth_users.router, prefix="/auth", tags=["auth"])
malliva_routers.include_router(
    malliva_users.router, prefix="/users", tags=["users"])
