import unittest
from auth import Auth
from user import User
from typing import Optional

auth = Auth()

USER_EMAIL = "hi"
USER_PASSWORD = "pw"

USER: User = auth.register_user(USER_EMAIL, "pw")


class TestAuth(unittest.TestCase):
    def test_session(self):
        USER_SESSION_ID: str = auth.create_session(USER_EMAIL)

        self.assertTrue(USER_SESSION_ID is not None)
        self.assertEqual(USER.session_id, USER_SESSION_ID)

    def test_get_user_from_session_id(self):
        USER_SESSION_ID: str = auth.create_session(USER_EMAIL)
        FOUND_USER: Optional[User] = auth.get_user_from_session_id(USER_SESSION_ID)

        self.assertIs(
            FOUND_USER,
            USER
        )

    def test_destroy_session(self):
        """
        Tests that calling 'AUTH.destroy_session(user_id)'
        replaces the User's 'session_id' value with None.
        """
        auth.create_session(USER_EMAIL)
        auth.destroy_session(USER.id)

        self.assertIs(USER.session_id, None)
