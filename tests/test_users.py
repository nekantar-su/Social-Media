import pytest
from app import schemas
from jose import jwt
from app.config import settings


def test_create_user(client):
    res = client.post("/users/",json={"email":"niko123@gmail.com","password":"1234"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "niko123@gmail.com"
    assert(res.status_code == 201)


def test_login_user(client,test_user):
    res = client.post("/login",data={"username":test_user["email"],"password":test_user["password"]})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token,settings.secret_key,algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert(res.status_code == 200)
    assert login_res.token_type == "bearer"
    assert id == test_user['id']

@pytest.mark.parametrize("email,password,status_code",[
    ("wrongemail@aol.com","pword123",403),
    ("wrongemail@aol.com","wrongpwrod123",403),
    (None,"pword123",403),
    ("nikokanta@aol.com",None,403),
])
def test_incorrect_login(client,email,password,status_code):
    res = client.post("/login", data={"username":email,"password":password})
    assert status_code == 403
