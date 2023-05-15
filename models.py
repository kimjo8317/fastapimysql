from passlib.context import CryptContext
from sqlalchemy import Column, TEXT, BIGINT, VARCHAR, DATETIME, BOOLEAN, Table, INT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
pwd_content = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "user"

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    username = Column(TEXT, nullable=False)
    password = Column(TEXT, nullable=False)
    name = Column(TEXT, nullable=False)
    phonenumber = Column(TEXT, nullable=False)
    email = Column(TEXT, nullable=False)
    birth = Column(TEXT, nullable=False)


class Questionboard(Base):
    __tablename__ = "questionboard"

    id = Column(BIGINT, primary_key=True, nullable=False, autoincrement=True)
    username = Column(TEXT, nullable=False)
    subject = Column(VARCHAR, nullable=False)
    content = Column(TEXT, nullable=False)
    create_date = Column(DATETIME, nullable=False)
    voter = relationship('user', backref='question_voters')


class Comment(Base):
    __tablename__ = "comment"

    id = Column(BIGINT, primary_key=True, autoincrement=True, nullable=False)
    username = Column(TEXT, nullable=False)
    comment = Column(TEXT, nullable=False)
    pri = Column(BOOLEAN, nullable=False)
    create_date = Column(DATETIME, nullable=False)
    pageid = Column(BIGINT, nullable=False)

#추천(ManyToMany방식) 베이스 테이블
question_voter = Table(
    'question_voter',
    Base.metadata,
    Column('user_id', BIGINT, nullable=False, primary_key=True),
    Column('question_id', INT, nullable=False)
)