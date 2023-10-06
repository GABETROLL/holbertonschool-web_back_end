#!/usr/bin/env python3
"""
Contains 'BasicAuth', which is an empty
child class of 'Auth'.
"""
from api.v1.auth.auth import Auth
from typing import TypeVar, List
import base64
import binascii
from models.user import User


class BasicAuth(Auth):
    """
    Has method 'self.current_user(request)',
    which takes in an HTTP request to this site,
    and returns a 'models.user.User' instance
    representing the user's credentials.

    If the request has an auth header,
    and the credentials are valid, the above
    paragraph is true.

    But if the credentials are invalid,
    there's anything wrong with the auth header
    or the auth header is missing, the method
    returns None.

    The method uses the other methods in this
    class to achieve its purpose.
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
        # print(user_email, user_pwd)

        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        
        # print("REAL CREDENTIALS")

        MATCHING_USERS: List[User] = User.search({"email": user_email, "password": user_pwd})

        # print(f"{MATCHING_USERS = }")

        if not MATCHING_USERS:
            return None

        elif len(MATCHING_USERS) == 1:
            return MATCHING_USERS[0]

        else:
            return None

    def current_user(self, request: str =None) -> TypeVar('User'):
        """
        Takes in an HTTP request AUTH HEADER,
        named 'request', to this site,
        and returns a 'models.user.User' instance
        representing the user's credentials.

        (THE 'request' VARIABLE IS ASSUMED TO BE
        THE USER REQUEST HEADER, AND IS ASSUMED TO BE
        SAFE AND VALID)

        If the headers, named 'request', have
        valid credentials, the above
        paragraph is true.

        But if the credentials are invalid,
        there's anything wrong with the auth header
        or the auth header is missing, the method
        returns None.

        The method uses the other methods in this
        class to achieve its purpose.
        """
        return self.user_object_from_credentials(
            *self.extract_user_credentials(
                self.decode_base64_authorization_header(
                    self.extract_base64_authorization_header(
                        request
                    )
                )
            )
        )
