from fastapi.encoders import jsonable_encoder
from services.authentication import authenticate
from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import JSONResponse
from schema.categories import Category
from models.categories import Category as CategoryModel
from config.config_loader import settings
from services.python_operations import convert_mongo_result_to_dict, loop_through_queryset
from dbConnectionManager.db_session import accounts_db_connection_instance

router = APIRouter()


@router.post("/", response_model=Category)
async def create_category(category: Category, request: Request):
    current_user = await authenticate(request)

    category = jsonable_encoder(category)

    try:
        instance = CategoryModel(
            **category).switch_db(settings.ACCOUNT_DEFAULT_ALIAS)
    except:
        raise HTTPException(detail="Marketplace database does not exist, please use the right marketplace address.",
                            status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    try:
        instance.save()
        instance = convert_mongo_result_to_dict(instance)
        instance = jsonable_encoder(Category(**instance))
        await accounts_db_connection_instance.end_db_connection()
        return JSONResponse(content=instance, status_code=status.HTTP_201_CREATED)
    except:
        raise HTTPException(detail="Listing could not be created",
                            status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.get("/", response_model=Category)
async def get_categories(skip: int = 0, limit: int = 100):
    return CategoryModel.objects.skip(skip).limit(limit)


@router.get("/{id}", response_model=Category)
async def get_category(id: int):
    return CategoryModel.objects.get(id=id)


@router.delete("/{id}", response_model=Category)
async def delete_category(id: int):
    category = CategoryModel.objects.get(id=id)
    category.delete()
    return category


@router.put("/{id}", response_model=Category)
async def update_category(id: int, category: Category):
    category.save()
    return category("/categories", response_model=Category)
