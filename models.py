from passlib.context import CryptContext
from sqlalchemy import Column, TEXT, BIGINT, VARCHAR, DATETIME,INT
from sqlalchemy.ext.declarative import declarative_base

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


#AI서버 연동할 테이블
class food(Base):
    __tablename__ = "food"
    id = Column(INT, primary_key=True, nullable=False, autoincrement=True)
    name = Column(TEXT, nullable=False)


#게시물 수정 삭제