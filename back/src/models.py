from enum import Enum
from typing import List
from pydantic import BaseModel, Field, field_validator
from uuid import UUID, uuid4


class UserEnum(int, Enum):
    USER = 0
    AGENT = 1


class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    type: UserEnum = UserEnum.USER or UserEnum.AGENT

    @field_validator('type')
    @classmethod
    def validate_type(cls, user_type: UserEnum):
        if not isinstance(user_type, Enum):
            raise ValueError('User type must be an Enum value: USER(0) or AGENT(1)')
        return user_type


class Message(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    author: User
    content: str

    @field_validator('author')
    @classmethod
    def validate_author(cls, author: User):
        if not isinstance(author, User):
            raise ValueError('author must be an instance of User')
        return author


class Chat(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    messages: List[Message] = []

    def alternate_author(self):
        if len(self.messages) >= 2:
            return self.messages[-2].author.type != self.messages[-1].author.type
        return True
