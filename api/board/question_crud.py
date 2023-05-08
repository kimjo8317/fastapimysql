from datetime import datetime
from main import Session
from models import Questionboard
from api.board.question_schema import questionCreate


# def get_question_list(db: Session):
#     question_list = db.query(questionCreate)\
#         .order_by(questionCreate.create_date.desc())\
#         .all()
#     return question_list
#
# def get_question(db: Session, question_id: int):
#     question = db.query(questionCreate).get(question_id)
#     return question

def create_question(db: Session, question_Create: questionCreate):
    db_createboard = Questionboard(
                           subject=question_Create.subject,
                           content=question_Create.content,
                           create_date=datetime.utcnow())
    db.add(db_createboard)
    db.commit()