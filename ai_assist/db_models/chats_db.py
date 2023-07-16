from datetime import datetime
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Chats(Base):
    __tablename__ = 'chats'

    chat_id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    user_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    title = Column(String(100))
    initial_message = Column(String(1000))
    created_at = Column(DateTime, default=datetime.now())


class Messages(Base):
    __tablename__ = 'messages'

    message_id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    chat_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    user_message = Column(String(1000))
    ai_message = Column(String(1000))
    message_time = Column(DateTime, default=datetime.now())
