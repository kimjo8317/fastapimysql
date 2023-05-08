from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware
from api.user import user_router
# from api.board import question_router
from database import engineconn



app = FastAPI() 

engine = engineconn() 
Session = sessionmaker(bind=engineconn)


origins = [
    "http://localhost",
    "http://localhost:3000"
]
# 프론트의 react 주소를 알려줌.

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

pwd_content = CryptContext(schemes=["bcrypt"],deprecated="auto")

app.include_router(user_router.router)
# app.include_router(question_router.router)

