from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from board import question_schema, question_crud
from database import get_db


router = APIRouter(
    prefix="/api/question",
)
@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.boardCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_board(db=db, board_create=_question_create)
@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question