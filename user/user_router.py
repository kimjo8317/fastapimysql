import logging
from datetime import timedelta, datetime
# from fastapi.security import OAuth2PasswordRequestForm
#API의username과 password의 값은 OAuth2PasswordRequestForm으로 얻어온뒤
#username을 사용하여 사용자 모델 객체(user)를 조회하여 가져옴
# from jose import jwt
#Json 포맷을 이용하여 사용자에 대한 속성을 저장하는 Claim 기반의 Web Token
from user.user_crud import pwd_context
#로그인라우터 OAuth2PasswordRequestForm  jwt 는 설치해야함
#pip install python-multipart
#pip install "python-jose[cryptography]"
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status
from database import get_db
from user import user_crud, user_schema
from user.user_crud import pwd_context
import secrets




ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "RS256"
#웹에서 openssl 다운받은뒤 C:\Program Files\OpenSSL-Win64
#환경 변수를 path = C:\Program Files\OpenSSL-Win64
#새로운변수 OPENSSL_CONF   /   C:\Program Files\OpenSSL-Win64\openssl.cfg
#설정 후 pip install pyOpenSSL 설치
#터미널에 openssl rand -hex 32 입력후 시크릿키 생성

## import secrets  //임포트시키는방법도있음
#secrets.token_hex(32)  //터미널입력
#'344a451d26d1968c0cd4ca12613e5f61b0f71dafced442c730edba55bb9035bc'



router = APIRouter(
    prefix="/api/user",
)
@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    user = user_crud.get_existing_user(db, user_create=_user_create)

    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")
    #HTTPException 함수는 HTTP 프로토콜을 사용하는 웹 서버에서 발생할 수 있는 예외 상황을 처리하기 위한 함수

    user_crud.create_user(db=db, user_create=_user_create)


# @router.post("/login", response_model=user_schema.Token)
# def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
#                            db: Session = Depends(get_db)):
#
#
#
#     user = user_crud.get_user(db, form_data.username)
#     if not user or not pwd_context.verify(form_data.password, user.password):
#     #pwd_context 의 verify함수는 암호화 되지 않은 비밀번호를 암호화하여 데이터베이스에 저장된 암호와 일치하는지 판단
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     # user 와 password 를 체크
#
#     data = {
#         "sub": user.username,
#         "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#
#     }
#     access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
#
#     return {
#         "access_token": access_token,
#         "token_type": "bearer",
#         "username": user.username
#     }
   # make access token