import secrets
from datetime import datetime, timedelta
import jwt
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status
from database import get_db
from api.user import user_schema, user_crud
from api.user.user_crud import pwd_context
from models import User

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"

router = APIRouter(
    prefix="/api/user",
)

#회원가입 API
@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    user = user_crud.create_user(db, user_create=_user_create)

    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")
    #HTTPException 함수는 HTTP 프로토콜을 사용하는 웹 서버에서 발생할 수 있는 예외 상황을 처리하기 위한 함수

#로그인 API
@router.post("/login", response_model=user_schema.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)):



    user = user_crud.get_user(db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.password):
    #pwd_context 의 verify함수는 암호화 되지 않은 비밀번호를 암호화하여 데이터베이스에 저장된 암호와 일치하는지 판단
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # user 와 password 를 체크

    data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }

#회원 수정 API
@router.patch("/{username}", status_code=status.HTTP_204_NO_CONTENT)
def update(
    username: str, user_update: user_schema.Updateuser, db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 일부 필드만 업데이트 (None이 아닌 값만 업데이트)
    update_data = user_update.dict(exclude_unset=True)
    for field in update_data:
        setattr(user, field, update_data[field])

    # 중복 검사
    # if db.query(User).filter(User.name == user_update.name).first():
    #     raise HTTPException(status_code=409, detail="Username already exists")

    db.commit()
    db.refresh(user)
    return {"message": "Successfully updated user"}
@router.get("/{username}")
async def read_user(
    username: str,
    db: Session = Depends(get_db),
):  # 값의 종류가 적을땐 파라미터로써 가져오는게 관리면에서 편하다.
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user.username

