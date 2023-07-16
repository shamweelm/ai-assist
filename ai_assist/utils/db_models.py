import uuid
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Chats(Base):
    __tablename__ = 'chats_test'

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    name = Column(String(100))
    question = Column(String(1000))
    model = Column(String(100))
    # Temperature is a float between 0 and 1
    temperature = Column(Float)
    # Max tokens is an integer between 1 and 2048
    max_tokens = Column(Integer)
