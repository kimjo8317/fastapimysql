from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from user import user_schema, user_crud

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