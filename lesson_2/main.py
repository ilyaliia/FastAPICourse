from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ConfigDict
import uvicorn

app = FastAPI()

data = {
    "email": "abc@mail.ru",
    "bio": "Биография",
    "age": 27,
    "gender": "male"
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)
    age: int = Field(ge=0, le=130)

    # model_config = ConfigDict(extra="forbid") # запрет неожиданных полей


user = UserSchema(**data)
# print(repr(user))

users = []


@app.post("/users", tags=["Пользователи"], summary="Добавление пользователя")
def add_user(user: UserSchema):
    users.append(user)
    return {"success": True, "message:": "Пользователь добавлен"}


@app.get("/users", tags=["Пользователи"], summary="Все пользователи")
def get_users() -> list[UserSchema]:
    return users


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
