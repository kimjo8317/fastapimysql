from datetime import datetime

from board.question_schema import board, questionCreate
from main import Session
from models import questionboard


def get_question_list(db: Session):
    question_list = db.query(questionboard)\
        .order_by(questionboard.create_date.desc())\
        .all()
    return question_list

def get_question(db: Session, question_id: int):
    question = db.query(questionboard).get(question_id)
    return question

def create_question(db: Session, board_create: questionCreate):
    db_questionboard = questionboard(
                           id=board_create.id,
                           subject=board_create.subject,
                           content=board_create.content,
                           create_date=datetime.now())
    db.add(db_questionboard)
    db.commit()