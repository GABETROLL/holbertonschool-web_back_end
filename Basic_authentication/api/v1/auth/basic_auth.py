#!/usr/bin/env python3
"""
Contains 'BasicAuth', which is an empty
child class of 'Auth'.
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
import base64
import binascii
from models.user import User


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
        "<user email> : <password>" when decoded.

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

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """
        'base64_authorization_header' IS ASSUMED TO BE RETURNED
        FROM 'self.extract_base64_authorization_header', AND IS ASSUMED
        TO BE VALID USER CERENDTIALS!!!

        If 'base64_authorization_header' is:
            None,
            not a 'str' (even if it's an instance of a child of 'str'),
            or not a valid Base64 encoding:
        THIS METHOD RETURNS NONE.

        Decodes and returns the <user email: password> credentials that are
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

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """
        'decoded_base64_authorization_header' IS ASSUMED TO BE RETURNED
        FROM 'self.decode_base64_authorization_header', AND IS ASSUMED
        TO BE VALID & SAFE USER CERENDTIALS!!!

        The format for 'decoded_base64_authorization_header' should be:
        <user email>:<password>.
        THIS METHOD ASSUMES THAT THERE'S ONLY ONE
        ':' IN 'decoded_base64_authorization_header'.

        If 'decoded_base64_authorization_header' is:
            None,
            not a 'str' (even if it's an instance of a child of 'str'),
            or doesn't contain ':':
        THIS METHOD RETURNS '(None, None)'.

        Returns the <user email: password> in
        'decoded_base64_authorization_header'
        as a tuple of their sub-strings individually.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) != str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        return tuple(
            decoded_base64_authorization_header.split(':')
        )

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        This method FIRST VALIDATES THAT THE ARGUMENT CREDENTIALS
        ARE VALID, in ', then returns an 'api.models.user.User'
        instance of the user that logged in.

        The credentials are valid if they're both part of
        THE SAME ROW in 'user_data.csv'.
        """
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        
        with open('user_data.csv') as user_data:
            try:
                header_line: str = next(user_data)
            except StopIteration:
                # CSV file was empty.
                return None

            try:
                user_email_index: int = header_line.split(",").index("email")
                user_pwd_index: int = header_line.split(",").index("password")
            except ValueError:
                # CSV file didn't contain the
                # 'email' nor 'password' columns.
                return None

            # Check for a row with that name and that password.
            while True:
                try:
                    split_line = next(user_data).split(",")
                except StopIteration:
                    break
                else:
                    if split_line[user_email_index] == user_email and split_line[user_pwd_index] == user_pwd:
                        return User(
                            email=user_email,
                            _password=user_pwd
                        )

            return None
