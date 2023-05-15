from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from starlette import status
from database import get_db
from fastapi.responses import JSONResponse, FileResponse
from models import User, Images
import boto3


router = APIRouter(
    prefix="/api/image",
)

S3_BUCKET_NAME = ""
S3_ACCESS_KEY = ""
S3_SECRET_KET = ""
S3_REGION = ""


s3_client = boto3.client(
    "s3",
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KET,
    region_name=S3_REGION,
)


@router.post("/uploadfile")
async def create_upload_file(
    filename: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    s3_client.upload_fileobj(file.file, S3_BUCKET_NAME, file.filename)

    file_url = f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{file.filename}"
    image = Images(filename=filename, url=file_url)
    db.add(image)
    db.commit()
    return {"url": file_url}
