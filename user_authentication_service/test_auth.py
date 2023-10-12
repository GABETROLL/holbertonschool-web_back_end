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

    def test_get_reset_password_token(self):
        """
        Tests that calling 'AUTH.get_reset_password_token(<user's email>)'
        sets the user's 'reset_token' value to the new token,
        and returns it.

        The User should be the one that has the email above as its 'email'
        value.

        If the user doesn't exist, 'AUTH.get_reset_password_token'
        should raise 'ValueError'.
        """
        auth.create_session(USER_EMAIL)

        TOKEN: str = auth.get_reset_password_token(USER_EMAIL)

        self.assertTrue(TOKEN is not None)
        self.assertEqual(TOKEN, USER.reset_token)

        self.assertRaises(
            ValueError,
            auth.get_reset_password_token,
            "DOESN'T EXIST"
        )

    def test_update_password(self):
        """
        Tests that 'AUTH.update_password(<token>)'
        updates the password of the USER.
        """
        TOKEN: str = auth.get_reset_password_token(USER_EMAIL)
        NEW_PASSWORD = "NEW PASSWORD"
        auth.update_password(TOKEN, NEW_PASSWORD)
        self.assertTrue(
            auth.valid_login(USER_EMAIL, NEW_PASSWORD)
        )
