import unittest
from auth import Auth
from user import User


class TestAuth(unittest.TestCase):
    def test_session(self):
        USER_EMAIL = "hi"

        auth = Auth()
        auth.register_user("hi", "pw")

        USER_SESSION_ID: str = auth.create_session(USER_EMAIL)
        USER: User = auth._db.find_user_by(email="hi")

        self.assertTrue(USER_SESSION_ID is not None)
        self.assertEqual(USER.session_id, USER_SESSION_ID)

