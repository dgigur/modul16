from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main_paige() -> dict:
    return {'message': 'Главная страница'}


@app.get('/user/admin')
async def admin_enter() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def user_enter(user_id) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user')
async def user_info(username: str, age: int) -> dict:
    return {'User': username, "Age": age}

