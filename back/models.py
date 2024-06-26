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
    def validate_type(cls, value: UserEnum):
        if not isinstance(value, Enum):
            raise ValueError('User type must be USER or AGENT')
        return value


class Message(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    author: User
    content: str


class Chat(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    messages: List[Message] = []

    def alternate_author(self):
        if len(self.messages) >= 2:
            return self.messages[-2].author.type != self.messages[-1].author.type
        return True
