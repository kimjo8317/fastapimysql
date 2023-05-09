from passlib.context import CryptContext
from sqlalchemy import Column, TEXT, INT, VARCHAR, DATE
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
pwd_content = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "user"

    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    username = Column(VARCHAR, nullable=False)
    password = Column(VARCHAR, nullable=False)
    name = Column(VARCHAR, nullable=False)
    phonenumber = Column(TEXT, nullable=False)
    email = Column(TEXT, nullable=False)
    birth = Column(DATE, nullable=False)

class Questionboard(Base):
    __tablename__ = "questionboard"

    id = Column(INT, primary_key=True, nullable=False, autoincrement=True)
    subject = Column(VARCHAR, nullable=False)
    content = Column(TEXT, nullable=False)
    create_date = Column(DATE, nullable=False)

class food(Base):
    __tablename__ = "food"
    id = Column(INT, primary_key=True, nullable=False, autoincrement=True)
    name = Column(TEXT, nullable=False)
