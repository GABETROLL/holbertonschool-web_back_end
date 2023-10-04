#!/usr/bin/env python3
"""
Exercise 5: Make a function that takes in a password string,
and returns the password salted and hashed using 'bcrypt.hashpw'.

The return type should be a byte string.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns the password salted and hashed,
    with 'bcrypt.hashpw(password.encode(), bcrypy.gensalt())'.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
