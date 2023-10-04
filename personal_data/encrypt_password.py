#!/usr/bin/env python3
"""
Exercise 5: Make a function that takes in a password string,
and returns the password salted and hashed using 'bcrypt.hashpw'.

The return type should be a byte string.

Exercise 6: Make a function that takes in the hashed and salted
version of a password, and a new string called 'password',
and checks if this new 'password' is valid, using 'bcrypt'.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns the password salted and hashed,
    with 'bcrypt.hashpw(password.encode(), bcrypy.gensalt())'.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Returns True if 'password' is valid,

    ASSUMING THAT:
    'hashed_password' is 'password' salted and hashed
    by 'hashed_password' or 'bcrypt', AND 'password'
    IS NOT STORED IN ANY DATABASE,
    ONLY 'hashed_password'.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
