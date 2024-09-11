from fastapi import FastAPI, Path, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def list_of_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def users_reg(user: User,
                    username: str = Path(min_length=3, max_length=20, description="Enter username", example='kolobok'),
                    age: int = Path(ge=18, description="Enter age", example=33)) -> User:
    if len(users) == 0:
        user.id = 1
    else:
        user.id = users[-1].id + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def users_update(user=Body(),
                       user_id: int = Path(gt=0, description='Enter id', example=2),
                       username: str = Path(min_length=3, max_length=20, description="Enter username",
                                            example='kolobok'),
                       age: int = Path(ge=18, description="Enter age", example=33)) -> User:
    for i in users:
        if i.id == user_id:
            i.username = username
            i.age = age
            return i
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def users_del(user_id: int = Path(gt=0, description='Enter id', example=2)) -> User:
    for i in users:
        if i.id == user_id:
            users.remove(i)
            return i
    raise HTTPException(status_code=404, detail="User was not found")
