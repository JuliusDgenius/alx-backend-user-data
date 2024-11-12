#!/usr/bin/env python3
"""Module defines the Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class Auth to manage API authentication"""
    def __init__(self) -> str:
        """Initialize the Auth object"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns a Bool"""
        return False

    def authorization_header(self, request=None) -> str:
    	"""Returns authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
    	"""Returns the current user"""
        return None
