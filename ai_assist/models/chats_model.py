from typing import Optional
from pydantic import BaseModel


class CreateChatRequest(BaseModel):
    model: str = "gpt-3.5-turbo-16k"
    question: str
    temperature: Optional[float] = 0.0
    max_tokens: Optional[int] = 256


class CreateChatResponse(BaseModel):
    status: str
    message: str
    data: dict

    