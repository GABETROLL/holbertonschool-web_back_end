#!/usr/bin/env python3
"""
Template to handle all authentication of this project/folder,
'Basic_authentication/'.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Template for all authentication systems
    implemented in this project, called 'Basic_authentication'.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None
