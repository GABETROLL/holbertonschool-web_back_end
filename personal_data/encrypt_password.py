#!/usr/bin/env python3
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns the password salted and hashed,
    with 'bcrypt.hashpw(password.encode(), bcrypy.gensalt())'.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
