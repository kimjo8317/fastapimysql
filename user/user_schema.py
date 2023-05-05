from pydantic import BaseModel, validator, EmailStr

class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    phonenumber: str
    email: str
    birth: str
    # EmailStr은 해당 값이 이메일 형식과 일치하는지 검증하기 위해 사용
    # pip install "pydantic[email]" 설치해야됨