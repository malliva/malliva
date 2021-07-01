from fastapi import APIRouter
from routers import malliva_users, auth_users, sitewide_seo, index_routes, listings


malliva_routers = APIRouter()


malliva_routers.include_router(
    auth_users.router, prefix="/auth", tags=["auth"])
malliva_routers.include_router(
    malliva_users.router, prefix="/users", tags=["users"])
malliva_routers.include_router(
    listings.router, prefix="/listings", tags=["listings"])
