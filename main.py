from fastapi import FastAPI
import requests
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware
from api.user import user_router
from api.board import question_router
from database import engineconn



app = FastAPI()

# AI 서버의 주소
AI_SERVER_URL = "http://127.0.0.1:8000"
@app.post("/predict")
async def predict(input_data: str):
    # AI 서버로 데이터 전송
    ai_server_response = requests.post(AI_SERVER_URL + "/predict", data=input_data)

    # AI 서버에서 받은 결과 반환
    return ai_server_response.text


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
app.include_router(question_router.router)

# if __name__ == "__main__":
#     port = os.getenv("PORT")
#     if not port:
#         port = 8080
#     uvicorn.run(app, host="0.0.0.0", port=8080)