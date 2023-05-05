from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import models
from database import engine
models.Base.metadata.create_all(bind=engine)



app = FastAPI()

origins = [
    "http://localhost:3000",    # 또는 "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

@app.get("/")
async def root():
    return {"message": "Hello World"}