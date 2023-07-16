import os
from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import StreamingResponse
from ai_assist.db_models.users_db import Users
from ai_assist.utils.db_operations import DatabaseOperations, db_client
from ai_assist.api_models.users_api import CreateUserRequest, CreateUserResponse

users_router = APIRouter()


# Create new chat route to accept a chat name and create a new chat
@users_router.post("/create_user", response_model=CreateUserResponse, tags=["Users"])
async def create_chat(request: CreateUserRequest):
    # Create a new user
    new_user = Users(
        name=request.name,
        email=request.email,
        model=request.model,
        location=request.location,
        temperature=request.temperature,
        max_tokens=request.max_tokens
    )

    # Insert the new chat into the database
    new_user_added = db_client.insert_record(new_user)

    # Retrieve the chat ID from the inserted record
    user_id = new_user_added.user_id
    print(user_id)
    print(type(user_id))

    # Return the response
    return CreateUserResponse(
        user_id=str(user_id),
        status="success",
        message="User created successfully",
        data={
            "name": request.name,
            "email": request.email,
            "location": request.location,
        },
    )
