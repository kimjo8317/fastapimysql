from fastapi import FastAPI
from database import engineconn
from models import User


app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()

@app.get("/")
async def root():
    example = session.query(User).all()
    return example
