from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    phonenumber: str
    email: str
    birth: str
    # pip install "pydantic[email]" 설치해야됨