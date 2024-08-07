#!/usr/bin/env python3
"""a module that defines the Auth class"""

from flask import request
from typing import (
        List,
        TypeVar
        )

class Auth:
    """class Auth definition"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth func definition"""
        return False


    def authorization_header(self, request=None) -> str:
        """authorization_header func definition"""
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """current_user func definition"""
        return None
