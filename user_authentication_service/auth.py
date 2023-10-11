#!/usr/bin/env python3
"""
Contains functionality to authenticate users
before interacting with the database.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Returns the salted and hashed version of 'password'
    using 'bcrypt'.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


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
