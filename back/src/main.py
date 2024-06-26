from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import Chat, Message, User, UserEnum

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    "http://localhost:3003",
    "http://localhost:3004",
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

agent = User(type=UserEnum.AGENT)


@app.post(
    '/',
    response_model=Message,
    status_code=status.HTTP_201_CREATED
)
async def send_message(chat: Chat):
    if len(chat.messages) > 0:
        is_alternated = chat.alternate_author()

        if is_alternated:
            message = Message(
                author=agent,
                content="This is a generated response to your message"
            )
            return message
        else:
            raise HTTPException(
                status_code=400,
                detail="You should wait for agent message before ask something else..."
            )
