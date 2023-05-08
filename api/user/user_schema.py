from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    phonenumber: str
    email: str
    birth: str

class Token(BaseModel):
    access_token: str
    token_type: str
    username: str