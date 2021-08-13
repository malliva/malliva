import json
from config.config_loader import settings
from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schema.listings import Listing
from models.listings import Listing as ListingModel, ListingImage
from models.custom_fields import CustomField, CustomFieldItem
from services.authentication import authenticate
from services.python_operations import convert_mongo_result_to_dict, loop_through_queryset
from dbConnectionManager.db_session import accounts_db_connection_instance

router = APIRouter()


@router.post("/", response_model=Listing)
async def create_listing(listing: Listing, request: Request):
    current_user = await authenticate(request)

    listing = jsonable_encoder(listing)

    try:
        instance = ListingModel(
            **listing).switch_db(settings.ACCOUNT_DEFAULT_ALIAS)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=f"Marketplace database does not exist. Error: "+str(e))

    try:
        instance.save()
        instance = convert_mongo_result_to_dict(instance)
        instance = jsonable_encoder(Listing(**instance))
        await accounts_db_connection_instance.end_db_connection()
        return JSONResponse(content=instance, status_code=status.HTTP_201_CREATED)
    except:
        raise HTTPException(detail="Listing could not be created",
                            status_code=status.HTTP_501_NOT_IMPLEMENTED)


# List all listings in the database
@router.get("/", response_model=Listing)
async def read_listings(request: Request):
    """
    Retrieve listings.
    """
    current_user = await authenticate(request)

    try:
        queryset = ListingModel.objects.all().using(
            settings.ACCOUNT_DEFAULT_ALIAS)
        queryset = loop_through_queryset(Listing, queryset)
        await accounts_db_connection_instance.end_db_connection()
        return JSONResponse(content=queryset, status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(detail="No listing foundError: "+str(e),
                            status_code=status.HTTP_404_NOT_FOUND)


@router.get("/{listing_id}", response_model=Listing)
async def read_listing(listing_id: str, request: Request):
    current_user = await authenticate(request)

    try:
        instance = ListingModel.objects.filter(id=listing_id).first().switch_db(
            settings.ACCOUNT_DEFAULT_ALIAS)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=f"Marketplace database does not exist. Error: "+str(e))

    try:
        instance = convert_mongo_result_to_dict(instance)
        print(type(instance))
        instance = jsonable_encoder(Listing(**instance))
        await accounts_db_connection_instance.end_db_connection()
        return JSONResponse(content=instance, status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(detail="Listing could not be found. Error: " + str(e),
                            status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{listing_id}", response_model=Listing)
async def update_listing(listing_id: str, request: Request):
    current_user = await authenticate(request)
    return {"listing_id": listing_id}


@router.delete("/{listing_id}")
async def delete_listing(listing_id: str, request: Request):
    current_user = await authenticate(request)

    try:
        instance = ListingModel.objects.filter(id=listing_id).first().switch_db(
            settings.ACCOUNT_DEFAULT_ALIAS)
    except:
        raise HTTPException(detail="Marketplace database does not exist, please use the right marketplace address.",
                            status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    try:
        instance.delete()
        await accounts_db_connection_instance.end_db_connection()
        return JSONResponse(content="The listing was deleted successfully", status_code=status.HTTP_200_OK)
    except:
        raise HTTPException(detail="Listing could not be deleted.",
                            status_code=status.HTTP_400_BAD_REQUEST)
