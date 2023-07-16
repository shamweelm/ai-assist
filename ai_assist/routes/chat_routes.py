import os
from uuid import UUID
from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import StreamingResponse
from ai_assist.db_models.chats_db import Chats, Messages
from ai_assist.utils.db_operations import DatabaseOperations, db_client
from ai_assist.api_models.chats_api import (
    CreateChatRequest, CreateChatResponse, AddChatResponse, AddChatRequest,
    GetChatRequest, GetChatResponse
)

chat_router = APIRouter()


# Create new chat route to accept a chat name and create a new chat
@chat_router.post("/create_chat", response_model=CreateChatResponse, tags=["Chat"])
async def create_chat(request: CreateChatRequest):
    # Create a new chat
    title = request.initial_message[:100]
    new_chat = Chats(
        user_id=request.user_id,
        title=title,
        initial_message=request.initial_message,
    )

    # Insert the new chat into the database
    new_chat_added = db_client.insert_record(new_chat)

    # Retrieve the chat ID from the inserted record
    chat_id = new_chat_added.chat_id

    # Pass initial_message and get response from AI
    # Add the message and AI response to messages
    new_message = Messages(
        chat_id=chat_id,
        user_id=request.user_id,
        user_message=request.initial_message,
        ai_message="Test Response"
    )

    # Insert the new message into the database
    _ = db_client.insert_record(new_message)

    # Return the response
    return CreateChatResponse(
        status="success",
        message="Chat created successfully",
        data={
            "chat_id": chat_id,
            "user_id": request.user_id,
        },
    )


# Add chat to existing chat
@chat_router.post("/add_chat", response_model=AddChatResponse, tags=["Chat"])
async def add_chat(request: AddChatRequest):
    # Pass question and get response from AI
    # Create a new chat
    new_message = Messages(
        chat_id=request.chat_id,
        user_id=request.user_id,
        user_message=request.message,
        ai_message="Test Response 2"
    )

    # Insert the new chat into the database
    new_message = db_client.insert_record(new_message)

    # Return the response
    return AddChatResponse(
        status="success",
        message="Chat created successfully",
        data={
            "chat_id": new_message.chat_id,
            "user_id": request.user_id,
            "message_id": new_message.message_id,
            "ai_response": new_message.ai_message,
        },
    )

# Get call with chat id as param to retrieve all chats based on a chat ID
@chat_router.get("/get_chat", response_model=GetChatResponse, tags=["Chat"])
async def get_chat(chat_id: UUID = Query(..., description="Chat ID")):
    # Create a query to retrieve the chat
    query = {"chat_id": chat_id}
    records = db_client.fetch_all_records(Messages, query)

    print(records)

    data = []
    for record in records:
        data.append({
            "message_id": record.message_id,
            "user_id": record.user_id,
            "user_message": record.user_message,
            "ai_message": record.ai_message,
        })

    # Return the response
    return GetChatResponse(
        status="success",
        message="Chat retrieved successfully",
        data=data
    )

