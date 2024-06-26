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


class ChatSystemConcurrencyTestCase(TestCase):
    def test_users_post_messages(self):
        response1 = client.post(
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

        response2 = client.post(
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

        response3 = client.post(
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

        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code, 201)
        self.assertEqual(response3.status_code, 201)

        obj = response1.json()
        self.assertIn('id', obj)
        self.assertEqual(obj['author']['type'], UserEnum.AGENT)
        self.assertEqual(obj['content'], "This is a generated response to your message")

        obj = response2.json()
        self.assertIn('id', obj)
        self.assertEqual(obj['author']['type'], UserEnum.AGENT)
        self.assertEqual(obj['content'], "This is a generated response to your message")

        obj = response3.json()
        self.assertIn('id', obj)
        self.assertEqual(obj['author']['type'], UserEnum.AGENT)
        self.assertEqual(obj['content'], "This is a generated response to your message")

