from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class CreateChatRequest(BaseModel):
    user_id: UUID
    initial_message: str


class CreateChatResponse(BaseModel):
    status: str
    message: str
    data: dict


class AddChatRequest(BaseModel):
    user_id: UUID
    chat_id: UUID
    message: str


class AddChatResponse(BaseModel):
    status: str
    message: str
    data: dict


class GetChatRequest(BaseModel):
    chat_id: UUID


class GetChatResponse(BaseModel):
    status: str
    message: str
    # Data is a list of dictionaries with 
    # # {
    #         "message_id": record.message_id,
    #         "user_id": record.user_id,
    #         "user_message": record.user_message,
    #         "ai_message": record.ai_message,
    #     }
    data: list