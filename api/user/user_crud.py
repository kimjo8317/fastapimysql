from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models import User
from api.user.user_schema import UserCreate, UserUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#회원가입
def create_user(db: Session, user_create: UserCreate):
    db_user = User(
                   username=user_create.username,
                   password=pwd_context.hash(user_create.password),
                   name=user_create.name,
                   phonenumber=user_create.phonenumber,
                   email=user_create.email,
                   birth=user_create.birth,
                   )
    db.add(db_user)
    db.commit()
def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) |
        (User.email == user_create.email)
    ).first()
#username 또는 email로 등록된 사용자가 있는지 조회하는 get_existing_user 함수
def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
#사용자명으로 사용자 모델 객체를 리턴하는 get_user 함수


#회원정보 수정
async def update_user(db: Session, username: str, user_Update: UserUpdate):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
        db_user.name = user_Update.name
        db_user.email = user_Update.email
        db_user.phonenumber = user_Update.phonenumber
        db_user.birth = user_Update.birth
    db.comit()
    db.refresh(db_user)
    return {"message": "Successfully updated user"}

#회원비밀번호 수정
async def update_password(username: str, password: str, db: Session):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.password = pwd_context.hash(password)
    if db_user.password == pwd_context.hash(password):
        raise HTTPException(status_code=404, detail="Duplicated Password")

    db.commit()
    db.refresh(db_user)
    return {"message": "Successfully updated user"}