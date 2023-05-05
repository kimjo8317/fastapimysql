from sqlalchemy import Column, TEXT, INT, VARCHAR, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "User"

    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    username = Column(VARCHAR, nullable=False)
    password = Column(VARCHAR, nullable=False)
    name = Column(VARCHAR, nullable=False)
    phonenumber = Column(TEXT, nullable=False)
    email = Column(TEXT, nullable=False)
    birth = Column(DATE, nullable=False)

