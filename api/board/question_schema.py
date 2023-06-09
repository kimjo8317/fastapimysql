from datetime import datetime

from pydantic import BaseModel, validator

class questionCreate(BaseModel):
    
    subject: str
    content: str
    create_date: datetime
    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
