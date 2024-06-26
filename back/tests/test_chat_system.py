from unittest import TestCase
from fastapi.testclient import TestClient

from main import app
from models import UserEnum

client = TestClient(
    app,
    # base_url="http://testserver",
    # raise_server_exceptions=True,
    # root_path="",
    # backend="asyncio",
    # backend_options=None,
    # cookies=None,
    # headers=None,
    # follow_redirects=True,
)


class ChatSystemTestCase(TestCase):
    def test_user_post_message(self):
        response = client.post(
            url="/",
            json={
                "messages": [
                    {
                        "author": {
                            "type": UserEnum.USER
                        },
                        "content": "Lorem ipsum indolore ..."
                    }
                ]
            }
        )

        self.assertEqual(response.status_code, 201)

        obj = response.json()
        self.assertIn('id', obj)
        self.assertEqual(obj['author']['type'], UserEnum.AGENT)
        self.assertEqual(obj['content'], "This is a generated response to your message")

    def test_user_post_messages_alternate(self):
        response = client.post(
            url="/",
            json={
                "messages": [
                    {
                        "author": {
                            "type": UserEnum.USER
                        },
                        "content": "Lorem ipsum indolore ..."
                    },
                    {
                        "author": {
                            "type": UserEnum.AGENT
                        },
                        "content": "This is a generated response to your message"
                    },
                    {
                        "author": {
                            "type": UserEnum.USER
                        },
                        "content": "Lorem ipsum indolore ..."
                    },
                    {
                        "author": {
                            "type": UserEnum.AGENT
                        },
                        "content": "This is a generated response to your message"
                    },
                    {
                        "author": {
                            "type": UserEnum.USER
                        },
                        "content": "Lorem ipsum indolore ..."
                    },
                ]
            }
        )

        self.assertEqual(response.status_code, 201)

        obj = response.json()
        self.assertIn('id', obj)
        self.assertEqual(obj['author']['type'], UserEnum.AGENT)
        self.assertEqual(obj['content'], "This is a generated response to your message")

    def test_user_post_messages_exception(self):
        response = client.post(
            url="/",
            json={
                "messages": [
                    {
                        "author": {
                            "type": UserEnum.USER
                        },
                        "content": "Lorem ipsum indolore ..."
                    },
                    {
                        "author": {
                            "type": UserEnum.USER
                        },
                        "content": "Lorem ipsum indolore ..."
                    }
                ]
            }
        )

        self.assertEqual(response.status_code, 400)

        obj = response.json()
        self.assertEqual(
            obj['detail'],
            "You should wait for agent message before ask something else..."
        )
