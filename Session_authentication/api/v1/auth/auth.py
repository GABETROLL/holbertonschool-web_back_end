#!/usr/bin/env python3
"""
Template to handle all authentication of this project/folder,
'Basic_authentication/'.
"""
import flask
from typing import List, TypeVar
import os


class Auth:
    """
    Template for all authentication systems
    implemented in this project, called 'Basic_authentication'.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        'path': the path the user is trying to request.

        'excluded_paths': the paths the user needs authentication
        when requesting them.

        THIS METHOD ASSUMES THAT ALL OF THE PATHS IN 'excluded_paths'
        END WITH A '/'.

        Returns weather or not the user CAN ENTER
        these paths WITHOUT auth.

        This method returns True if 'path' is None
        or 'excluded_paths' is None or empty.
        """
        if path is None or excluded_paths is None:
            return True

        if not path.endswith('/'):
            path += '/'

        return path not in excluded_paths

    def authorization_header(self, request: flask.Request = None) -> str:
        """
        'request' IS ASSUMED TO BE
        THE FLASK 'request' VARIABLE.

        If 'request' is None, this method just returns None.

        Returns the request's authorization header.
        If it's None, that means there was no
        authorization header sent.
        """
        if request is None:
            return None

        result = request.headers.get('authorization')

        return result

    def current_user(self, request: str = None) -> TypeVar('User'):
        """
        Should return the 'models.user.User' object
        representing the user's email and password
        credentials, which IS ASSUMED TO BE SENDING
        OUR WEBSITE A REQUEST, 'request'.

        (I believe 'request' IS ASSUMED TO BE
        'flask.request')
        """
        return None

    def session_cookie(self, request: flask.Request = None):
        """
        ASSUMING THAT 'request' IS:
            THE USERS' SAFE AND VALID REQUEST
            'flask.request'
        AND THAT 'request.cookies' HAS THE COOKIE,

        this method returns value of
        the user's session ID cookie
        in the request.

        The name of the session cookie is ASSUMED to be
        the "SESSION_NAME" environment variable,
        in this computer, which is the server.
        """
        if request is None:
            return None

        return request.cookies.get(
            os.environ.get("SESSION_NAME", None)
        )
