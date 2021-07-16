from fastapi import APIRouter
from routers import (malliva_users,
                     auth_users,
                     sitewide_seo,
                     index_routes,
                     listings,
                     media_routes,
                     malliva_accounts,
                     custom_codes,
                     custom_fields,
                     transactions,
                     marketplace_settings,
                     categories
                     )


# router for main platform

malliva_routers = APIRouter()

# these are platform routes
malliva_routers.include_router(
    index_routes.router, tags=["index"])
malliva_routers.include_router(
    sitewide_seo.router, tags=["seo_routes"])
malliva_routers.include_router(
    auth_users.router, prefix="/auth", tags=["auth"])
malliva_routers.include_router(
    malliva_users.router, prefix="/users", tags=["users"])
malliva_routers.include_router(
    malliva_accounts.router, prefix="/marketplaces", tags=["marketplace accounts"])

# Media routes
malliva_routers.include_router(
    media_routes.router, prefix="/media", tags=["uploads"])


# these are routes available to marketplace accounts
sub_malliva_routers = APIRouter()

sub_malliva_routers.include_router(
    index_routes.router, tags=["index"])
sub_malliva_routers.include_router(
    sitewide_seo.router, tags=["seo_routes"])

sub_malliva_routers.include_router(
    auth_users.router, prefix="/auth", tags=["auth"])
sub_malliva_routers.include_router(
    malliva_users.router, prefix="/users", tags=["users"])
sub_malliva_routers.include_router(
    listings.router, prefix="/listings", tags=["listings"])
malliva_routers.include_router(
    custom_fields.router, prefix="/custom_fields", tags=["custom fields"])

# Media routes
sub_malliva_routers.include_router(
    media_routes.router, prefix="/media", tags=["uploads"])
