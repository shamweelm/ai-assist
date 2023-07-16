from typing import Optional
from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    name: str
    email: str
    location: str
    model: str
    temperature: float = 0.0
    max_tokens: int = 256


class CreateUserResponse(BaseModel):
    user_id: str
    status: str
    message: str
    data: dict
