from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from models import Chat, Message, User, UserEnum

app = FastAPI()

agent = User(type=UserEnum.AGENT)


@app.post(
    '/',
    response_model=Message,
    status_code=201
)
async def send_message(chat: Chat):
    if len(chat.messages) > 0:
        last_message = chat.messages[-1]
        is_alternated = chat.alternate_author(last_message)

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
