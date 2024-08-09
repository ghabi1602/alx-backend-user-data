#!/usr/bin/env python3
"""a module that defines a new authentication mechanism"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """a new class that manages session authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
            a method that creates a session ID for a user_id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        id = uuid.uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
            a method that returns a user ID based on a session ID
        """
        if session_id is None or not instance(session_id, str):
            return None
        
        return self.user_id_by_session_id.get('session_id')
