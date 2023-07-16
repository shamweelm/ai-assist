import os
from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import StreamingResponse
from ..utils.db_models import Chats
from ..utils.db_operations import DatabaseOperations, db_client
from ..models.chats_model import CreateChatRequest, CreateChatResponse

chat_router = APIRouter()


# Create new chat route to accept a chat name and create a new chat
@chat_router.post("/create_chat", response_model=CreateChatResponse, tags=["Chat"])
async def create_chat(request: CreateChatRequest):
    # Create a new chat
    name = request.question[:100]
    new_chat = Chats(
        name=name,
        question=request.question,
        model=request.model,
        temperature=request.temperature,
        max_tokens=request.max_tokens
    )

    # Insert the new chat into the database
    new_chat_added = db_client.insert_record(new_chat)

    # Retrieve the chat ID from the inserted record
    chat_id = new_chat_added.id

    # Return the response
    return CreateChatResponse(
        status="success",
        message="Chat created successfully",
        data={
            "chat_id": chat_id
        },
    )
