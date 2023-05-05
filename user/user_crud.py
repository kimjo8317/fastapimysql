from passlib.context import CryptContext
#passlib 라이브러리에서 제공하는 함수로, 비밀번호 해싱과 검증을 쉽게 처리할 수 있도록 도와줌
from sqlalchemy.orm import Session
from user.user_schema import UserCreate
from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#bcrypt 알고리즘을 사용하는 pwd_context 객체를 생성하고 pwd_context 객체를 사용하여 비밀번호를 암호화하여 저장

#회원정보의 비밀번호는 암호화하여야함 passlib설치

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
#사용자명 또는 이메일 값이 이미 존재하는지 확인함 (username과 email이 OR 조건임에 주의하자)


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
#사용자명으로 사용자 모델 객체를 리턴하는 get_user 함수

