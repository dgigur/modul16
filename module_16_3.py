from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def list_of_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def users_reg(username: str = Path(min_length=3, max_length=20, description="Enter username", example='kolobok'),
                    age: int = Path(ge=18, description="Enter age", example=33)) -> str:
    current_index = str(int(max(users, key=int))+1)
    users[current_index] = f"Имя: {username}, возраст: {str(age)}"
    return f"User {current_index} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def users_update(user_id: int = Path(gt=0, description='Enter id', example=2),
                       username: str = Path(min_length=3, max_length=20, description="Enter username", example='kolobok'),
                       age: int = Path(ge=18, description="Enter age", example=33)) -> str:
    users[str(user_id)] = f"Имя: {username}, возраст: {str(age)}"
    return f"The user {user_id} has been updated"


@app.delete('/user/{user_id}')
async def users_del(user_id: int = Path(gt=0, description='Enter id', example=2)) -> str:
    del users[str(user_id)]
    return f'user {user_id} has been deleted'
