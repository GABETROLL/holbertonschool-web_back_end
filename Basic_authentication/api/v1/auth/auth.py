#!/usr/bin/env python3
"""
Template to handle all authentication of this project/folder,
'Basic_authentication/'.
"""
import flask
from typing import List, TypeVar


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

        Returns True if 'path' is not inside 'excluded_paths'.
        IF 'path' DOESN'T END WITH A '/', 'path' FIRST GETS
        THE ENDING '/' BEFORE CHECKING.

        If 'path' is in 'excluded_paths', the user needs
        authentication when requesting it.
        If it's not in 'excluded_paths',
        the user doesn't need authentication when requesting it.

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
        Authorization header.
        'request' IS ASSUMED TO BE
        THE FLASK 'request' VARIABLE.
        """
        if request is None:
            return None

        if request.authorization is None:
            return None

        return request.authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user........
        """
        return None
