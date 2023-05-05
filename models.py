from sqlalchemy import Column, INTEGER, DATETIME, ForeignKey, VARCHAR, TEXT
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "User"

    id = Column(INTEGER, nullable=False, autoincrement=True, primary_key=True)
    username = Column(TEXT, nullable=False)
    password = Column(TEXT, nullable=False)
    name = Column(TEXT, nullable=False)
    phonenumber = Column(TEXT, nullable=False)
    email = Column(TEXT, nullable=False)
    birth = Column(TEXT, nullable=False)

