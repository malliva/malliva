from fastapi.testclient import TestClient
from main import malliva_api, sub_malliva_api

client = TestClient(malliva_api)

fake_user_db = {"user": {
    "_id": 35,
    "first_name": "John",
    "last_name": "Olubiyi",
    "username": "john1",
    "password": "$2b$12$tCjU9fYt4chlRI/kM/ajZ..vlfIDS3jJcP1cP0WWItIeko0Hk02i2",
    "email": "b@b2.com",
    "is_active": True,
    "is_superuser": False,
    "is_deleted": False,
    "terms_of_service_accepted": False,
    "created_at": "2021-07-07T20:54:19.578Z",
    "updated_at": "2021-07-07T20:54:19.578Z",
    "profile_picture": "localhost/users/john1"
},
    "user": {
    "_id": 36,
    "first_name": "John",
    "last_name": "Olubiyi432",
    "username": "john",
    "password": "$2b$12$lTXZ8d22SFVpwTrEBX3UIuM59uZcrDaZrTG4hyi5A34QZs60rQP4.",
    "email": "b@b13.com",
    "is_active": True,
    "is_superuser": False,
    "is_deleted": False,
    "terms_of_service_accepted": False,
    "created_at": "2021-07-07T21:05:20.922Z",
    "updated_at": "2021-07-07T21:05:20.922Z"
}
}


def test_create_user():
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
