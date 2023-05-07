from passlib.context import CryptContext
from sqlalchemy.orm import Session

from models import User
from user.user_schema import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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
    #회원데이터 저장

def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) |
        (User.email == user_create.email)
    ).first()
#username 또는 email로 등록된 사용자가 있는지 조회하는 get_existing_user 함수
