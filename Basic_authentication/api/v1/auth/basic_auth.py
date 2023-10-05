#!/usr/bin/env python3
"""
Contains 'BasicAuth', which is an empty
child class of 'Auth'.
"""
from api.v1.auth.auth import Auth
import base64
import binascii


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

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        'base64_authorization_header' IS ASSUMED TO BE RETURNED
        FROM 'self.extract_base64_authorization_header', AND IS ASSUMED
        TO BE VALID USER CERENDTIALS!!!

        If 'base64_authorization_header' is:
            None,
            not a 'str' (even if it's an instance of a child of 'str'),
            or not a valid Base64 encoding:
        THIS METHOD RETURNS NONE.

        Decodes and returns the <username: password> credentials that are
        encoded in 'base64_authorization_header', in Base64.
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None

        try:
            return base64.b64decode(base64_authorization_header).decode()
        except binascii.Error:
            return None
