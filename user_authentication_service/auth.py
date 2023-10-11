#!/usr/bin/env python3
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Returns the salted and hashed version of 'password'
    using 'bcrypt'.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

