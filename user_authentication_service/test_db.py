import unittest
from db import DB
from user import User

db = DB()
db.add_user("hi", "<hashed pasword>")
USER: User = db.find_user_by(email="hi")


class TestUpdateUser(unittest.TestCase):
    def test_correct_attrs(self):
        """
        Checks that 'db.update_user' properly changes the 'hashed_password'
        and 'session_id' attributes of a User instance.
        """
        USER_PASSWORD = "NEW PASSWORD"
        db.update_user(USER.id, hashed_password=USER_PASSWORD)
        self.assertEqual(USER.hashed_password, USER_PASSWORD)

        USER_SESSION_ID = "<session id>"
        db.update_user(USER.id, session_id=USER_SESSION_ID)
        self.assertEqual(USER.session_id, USER_SESSION_ID)

    def test_wrong_attr(self):
        """
        Makes sure that when 'db.update_user' is called with
        attributes that don't exist in the 'User' model,
        'db.update_user' doesn't update
        anything, and raises an AttributeError.
        """
        self.assertRaises(
            ValueError,
            db.update_user,
            USER.id,
            bad_attr=None
        )

        self.assertTrue("bad_attr" not in USER.__dict__)
