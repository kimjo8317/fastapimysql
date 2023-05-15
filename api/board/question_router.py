from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from api.board.question_schema import QuestionCreate, QuestionUpdate, BoardVote
from models import Questionboard

router = APIRouter(
    prefix="/api/board",
)


@router.post("/{username}/createboard", tags=["QAboard"], status_code=status.HTTP_200_OK)
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

#게시물 좋아요 기능
@router.post("/vote", status_code=status.HTTP_204_NO_CONTENT)
def answer_vote(_board_vote:BoardVote,
                db: Session = Depends(get_db),
                ):
    db_BoardVote = BoardVote(db, voter_id=_board_vote.voter_id)
    if not db_BoardVote:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    BoardVote(db, db_answer=db_BoardVote)


@router.get("/getboard", tags=["QAboard"])
def get_question(db: Session = Depends(get_db)):
    db_board = db.query(Questionboard).all()
    return db_board


@router.get("/detail/{username}", tags=["UserInfo"], status_code=status.HTTP_200_OK)
def my_detail(username: str, db: Session = Depends(get_db)):
    detail = db.query(Questionboard).filter(Questionboard.username == username).all()
    return detail


@router.patch("/update/{username}/{id}", status_code=status.HTTP_200_OK)
def question_update(
    username: str,
    id: int,
    question_update: QuestionUpdate,
    db: Session = Depends(get_db),
):
    question = (
        db.query(Questionboard)
        .filter(Questionboard.username == username, Questionboard.id == id)
        .first()
    )

    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Question not found"
        )

    update_data = question_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(question, key, value)

    db.commit()
    db.refresh(question)
    return {"message": "Successfully updated question"}


# 게시물 삭제기능
@router.delete("/delete/{id}", tags=["QAboard"])
def delete_board(id: int, db: Session = Depends(get_db)):
    id = db.query(Questionboard).filter(Questionboard.id == id).first()
    if not id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(id)
    db.commit()
