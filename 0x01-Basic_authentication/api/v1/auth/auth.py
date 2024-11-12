#!/usr/bin/env python3
"""Module defines the Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class Auth to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns a Bool"""
        if path is None or excluded_paths is None or not len(excluded_paths):
        	return True
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if p.endswith('*'):
                if p.startswith(p[:1]):
                    return False
        return False if path in excluded_paths else True


    def authorization_header(self, request=None) -> str:
        """Returns authorization header"""
        if request:
        	return request.header.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user"""
        return None
