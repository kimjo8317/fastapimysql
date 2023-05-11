from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from api.board import question_schema, question_crud
from database import get_db
from models import Questionboard, User
from api.board.question_schema import QuestionCreate


router = APIRouter(
    prefix="/api/board",
)

#게시물등록
@router.post(
    "/{username}/createboard", tags=["QAboard"], status_code=status.HTTP_200_OK
)
def create_question(
    username: str, question_Create: QuestionCreate, db: Session = Depends(get_db)
):
    db_createboard = Questionboard(
        username=username,
        subject=question_Create.subject,
        content=question_Create.content,
        create_date=question_Create.create_date,
    )
    db.add(db_createboard)
    db.commit()


@router.get("/getboard", tags=["QAboard"])
def get_question(db: Session = Depends(get_db)):
    db_board = db.query(Questionboard).all()
    return db_board


@router.get("/detail/{username}", tags=["UserInfo"], status_code=status.HTTP_200_OK)
def my_detail(username: str, db: Session = Depends(get_db)):
    detail = db.query(Questionboard).filter(Questionboard.username == username).all()
    return detail


#게시물 수정기능
@router.patch("/update/{username}", status_code=status.HTTP_204_NO_CONTENT)
def question_update(username : str, subject : str,question_update : question_schema.QuestionUpdate,db: Session = Depends(get_db)):
    question = db.query(Questionboard).filter(Questionboard.username == username,
                                              Questionboard.subject == subject).first()

    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")

    update_data = question_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(question, key, value)


    db.commit()
    db.refresh(question)
    return {"message": "Successfully updated question"}
#게시물 삭제기능
@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def answer_delete(_question_delete: question_schema.QuestionDelete,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(User)):
    db_answer = get_question(db, answer_id=_question_delete.question_id)
    if not db_answer:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_answer.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    _question_delete(db=db, db_answer=db_answer)