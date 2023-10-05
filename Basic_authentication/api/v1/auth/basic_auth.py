#!/usr/bin/env python3
"""
Contains 'BasicAuth', which is an empty
child class of 'Auth'.
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    Empty child class of 'Auth'
    """
    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        """
        The format for 'authorization_header' should be:
        "Basic <base 64>", and this method
        returns the <base 64> part, which should be
        "<username> : <password>" when decoded.

        If 'authorization_header' doesn't start with "Basic ",
        or 'authorization_header' isn't of type 'str'
        (even if it's a child class of 'str'),
        or 'authorization_header' is None,
        this method returns None.

        Returns the <base 64> part, WITHOUT DECODING IT.
        """
        HEADER_START = "Basic "

        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith(HEADER_START):
            return None

        return authorization_header[len(HEADER_START):]
