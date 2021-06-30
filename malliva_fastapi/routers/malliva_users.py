from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from models.mallivaUsers import User

router = APIRouter()


@router.post("/")
async def create_user(user: User):
    return user


@router.get("/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}


# List all Users in the database
@router.get("/", response_model=User)  # List[User])
def read_users(
    # db: Session = Depends(deps.get_db),
    # skip: int = 0,
    # limit: int = 100,
    users: User
    # current_user: models.User = Depends(deps.get_current_active_superuser),
):  # -> Any:
    """
    Retrieve users.
    """
    # users = crud.user.get_multi(skip=skip, limit=limit)
    return users


@router.put("/me")
async def update_user_me():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.put("/{username}")
async def update_user():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.delete("/me")
async def delete_user_me():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.delete("/{username}")
async def delete_user():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.delete("/")
async def delete_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
