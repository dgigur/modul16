from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/')
async def main_paige() -> str:
    return 'Главная страница'
    #return {'message': 'Главная страница'}


@app.get('/user/admin')
async def admin_enter() -> str:
    return 'Вы вошли как администратор'
    #return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def user_enter(user_id: Annotated[int, Path(ge=1,
                                                  le=100,
                                                  description='Enter User ID',
                                                  example=4)]) -> str:
    return f'Вы вошли как пользователь № {user_id}'
    #return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user/{username}/{age}')
async def user_info(username: Annotated[str, Path(min_length=5,
                                                  max_length=20,
                                                  description="Enter username",
                                                  example='kabachok')],
                    age: Annotated[int, Path(ge=18,
                                             le=120,
                                             description="Enter age",
                                             example=25)]) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
    # return {'User': username, "Age": age}