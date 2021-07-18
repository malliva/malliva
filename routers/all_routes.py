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
                     categories,
                     reviews_ratings,
                     orders,
                     payment_gateways,
                     messages,
                     malliva_emails
                     )


# router for main platform

malliva_routers = APIRouter()

# these are platform routes
malliva_routers.include_router(
    index_routes.router, tags=["Index"])
malliva_routers.include_router(
    sitewide_seo.router, tags=["Seo routes"])
malliva_routers.include_router(
    auth_users.router, prefix="/auth", tags=["Auth"])
malliva_routers.include_router(
    malliva_users.router, prefix="/users", tags=["Users"])
malliva_routers.include_router(
    malliva_accounts.router, prefix="/marketplaces", tags=["Marketplace accounts"])
# Media routes
malliva_routers.include_router(
    media_routes.router, prefix="/media", tags=["Uploads"])


# these are routes available to marketplace accounts
sub_malliva_routers = APIRouter()

sub_malliva_routers.include_router(
    index_routes.router, tags=["Index"])
sub_malliva_routers.include_router(
    sitewide_seo.router, tags=["Seo routes"])

sub_malliva_routers.include_router(
    auth_users.router, prefix="/auth", tags=["Auth"])
sub_malliva_routers.include_router(
    malliva_users.router, prefix="/users", tags=["Users"])
sub_malliva_routers.include_router(
    listings.router, prefix="/listings", tags=["Listings"])
sub_malliva_routers.include_router(
    categories.router, prefix="/categories", tags=["Categories"])
sub_malliva_routers.include_router(
    custom_fields.router, prefix="/custom_fields", tags=["Custom fields"])
sub_malliva_routers.include_router(
    reviews_ratings.router, prefix="/reviews", tags=["Reviews and ratings"])
sub_malliva_routers.include_router(
    transactions.router, prefix="/transactions", tags=["Transactions"])
sub_malliva_routers.include_router(
    orders.router, prefix="/orders", tags=["Orders"])
sub_malliva_routers.include_router(
    messages.router, prefix="/messages", tags=["Messages"])
sub_malliva_routers.include_router(
    malliva_emails.router, prefix="/emails", tags=["Malliva Emails"])
sub_malliva_routers.include_router(
    payment_gateways.router, prefix="/payment_gateways", tags=["Payment Gateways"])
sub_malliva_routers.include_router(
    custom_codes.router, prefix="/custom_codes", tags=["Custom codes"])
sub_malliva_routers.include_router(
    marketplace_settings.router, prefix="/settings_manager", tags=["Marketplace settings"])

# Media routes
sub_malliva_routers.include_router(
    media_routes.router, prefix="/media", tags=["Uploads"])
