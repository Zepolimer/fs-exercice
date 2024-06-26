from enum import Enum
from typing import List
from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class UserEnum(int, Enum):
    USER = 0
    AGENT = 1


class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    type: UserEnum = UserEnum.USER or UserEnum.AGENT


class Message(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    author: User
    content: str


class Chat(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    messages: List[Message] = []

    def alternate_author(self, last_message: Message):
        if len(self.messages) > 1:
            return self.messages[-1].author.type != last_message.author.type
        return True
