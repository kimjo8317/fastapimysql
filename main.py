from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from database import engineconn
from models import User
from user import user_router
# models.Base.metadata.create_all(bind=engine)



app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()

origins = [
    "http://localhost:3000",
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
    example = session.query(User).all()
    return example




app.include_router(user_router.router)
