from fastapi import FastAPI, Query, Path
from typing import Optional
from config.config_loader import settings
from dbConnectionManager.tenant_connections import connect_to_database
from models.items import Item

# initialize FastAPI

malliva_api = FastAPI(title=settings.APP_NAME,
                      description="This is a very fancy project, with auto docs for the API and everything",
                      version="1.0",)


@malliva_api.post("/items/")
async def create_item(item: Item):
    return item


@malliva_api.get("/items/")
async def read_items(q: Optional[str] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@malliva_api.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: Optional[str] = None,
    item: Optional[Item] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


@malliva_api.get('/info/')
async def info():
    return {
        "app_name": settings.APP_NAME,
        "debug": settings.DEBUG,
        "allowed_image_types": settings.ALLOWED_IMAGE_TYPES,
        "allowed_file_types": settings.ALLOWED_FILE_TYPES,
    }
