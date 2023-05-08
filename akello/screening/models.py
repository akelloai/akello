from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel



class Measurement(BaseModel):
    account_id: str
    user_id: str
    type: str
    data: dict

class Option(BaseModel):
    name: str
    value: str

class Question(BaseModel):
    score: Optional[int] = 0
    key: Optional[str] = None
    question: str
    options: List[Option] = []
    responses: List[str] = []


class Screener(BaseModel):
    name: str
    score: Optional[int] = 0
    questions: List[Question] = []

