from datetime import datetime
from main import Session
from models import questionboard
from board.question_schema import questionCreate


# def get_question_list(db: Session):
#     question_list = db.query(questionboard)\
#         .order_by(questionboard.create_date.desc())\
#         .all()
#     return question_list
#
# def get_question(db: Session, question_id: int):
#     question = db.query(questionboard).get(question_id)
#     return question

def create_question(db: Session, question_Create: questionCreate):
    db_createboard = questionboard(
                           subject=question_Create.subject,
                           content=question_Create.content,
                           create_date=datetime.now())
    db.add(db_createboard)
    db.commit()