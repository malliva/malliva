from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from schema.listings import Listing

router = APIRouter()


@router.post("/")
async def create_listing(listing: Listing):
    return listing


@router.get("/{listing_id}", tags=["listings"])
async def read_listing(listing_id: str):
    return {"listing_id": listing_id}


# List all listings in the database
@router.get("/", response_model=Listing)  # List[listing])
def read_listings(
    # db: Session = Depends(deps.get_db),
    # skip: int = 0,
    # limit: int = 100,
    listings: Listing
    # current_listing: models.listing = Depends(deps.get_current_active_superlisting),
):  # -> Any:
    """
    Retrieve listings.
    """
    # listings = crud.listing.get_multi(skip=skip, limit=limit)
    return listings


@router.put("/{listing_id}")
async def update_listing():
    return [{"listing_id": listing_id}, {"listing_id": listing_id}]


@router.delete("/{listing_id}")
async def delete_listing():
    return [{"listing_id": listing_id}, {"listing_id": listing_id}]
