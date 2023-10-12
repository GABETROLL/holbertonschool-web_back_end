#!/usr/bin/env python3
"""
Contains functionality to authenticate users
before interacting with the database.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Optional


def _hash_password(password: str) -> bytes:
    """
    Returns the salted and hashed version of 'password'
    using 'bcrypt'.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Returns the 'str' representation of
    'uuid.uuid5()'.
    """
    return str(uuid.uuid4())


class Auth:
    """
    To authenticate users before interacting with the database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        If a user with 'email' as its email already exists
        in 'sels' DB, this method raises ValueError.

        Otherwise, this hashes 'password' using 'bcrypt',
        adds the new 'User' to the DB with its hashed password,
        and returns it.
        """
        try:
            ALREADY_EXISTING_USER: User = self._db.find_user_by(email=email)
        except NoResultFound:
            # No user with same 'email' already exists
            HASHED_PASSWORD = _hash_password(password)
            return self._db.add_user(email, HASHED_PASSWORD)
        else:
            # User with same 'email' already exists
            raise ValueError(f"User {email} already exists.")

    def valid_login(self, email: str, password: str) -> bool:
        """
        ASSUMING that 'email' and 'password' are valid and safe,

        Returns weather or not the login credentials are correct.

        Returns True if a User with 'email' as its email
        and 'password' as its password exists in the DB.
        (THE PASSWORDS ARE HASHED)

        If the user with 'email' as its email doesn't exist,
        this method returns False.

        After validating the email, this method
        checks the password with 'bcrypt.checkpw'. If the password
        is invalid, this method returns False.
        """
        try:
            MAYBE_USER: User = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(
                password.encode(),
                MAYBE_USER.hashed_password
            )

    def create_session(self, email: str) -> Optional[str]:
        """
        Creates an new session ID for the user
        with 'email' as its 'email',

        and sets the User's 'session_id' value to it
        to keep track of its session,

        and returns the ID.

        If the user doesn't exist, this method just returns None.
        """
        try:
            USER_TO_LOGIN: User = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            USER_SESSION_ID: str = _generate_uuid()
            self._db.update_user(USER_TO_LOGIN.id, session_id=USER_SESSION_ID)
            return USER_SESSION_ID

    def get_user_from_session_id(self, session_id: str) -> Optional[str]:
        """
        ASSUMING that 'session_id' is a valid and safe session ID
        that MAY belong to a user who is logged in using SESSION AUTH,

        this method returns the corresponding user to that
        'session_id', in 'self's DB.

        If no user has a session with 'session_id' as the session's ID
        in 'self's DB, this method returns None.
        """
        try:
            RESULT: User = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return RESULT

    def destroy_session(self, user_id: int) -> None:
        """
        ASSUMING that 'user_id' is valid and safe,

        This method
        destroys the session of the user that has 'user_id's value
        as its 'id'.

        If the User doesn't exist, this method does nothing.
        """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """
        If a User with 'email's value as its 'email'
        doesn't exist in 'self's DB, this method raises ValueError.

        Otherwise, this method returns makes a new reset token,
        sets the User's 'reset_token' value to the token,
        and returns the token.
        """
        try:
            USER: User = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError(f"User with email={email} doesn't exist.")

        USER_RESET_TOKEN: str = _generate_uuid()
        self._db.update_user(USER.id, reset_token=USER_RESET_TOKEN)

        return USER_RESET_TOKEN

    def update_password(self, reset_token: str, password: str) -> None:
        """
        If the 'reset_token' belongs to a user if self's DB,
        this method sets the User's 'password' value to the hashed
        version of 'password'.

        If the 'reset_token' doesn't belong to any 'User' in self's DB,
        this method doesn't change the password.
        """
        try:
            USER: User = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError(f"Invalid password reset token: {reset_token}")

        HASHED_PASSWORD: str = _hash_password(password)

        try:
            self._db.update_user(
                USER.id, reset_token=None, hashed_password=HASHED_PASSWORD
            )
        except (NoResultFound, ValueError, Exception):
            # These are not supposed to happen, since we already found
            # the 'USER' above.

            # Printing them just in case.
            raise
