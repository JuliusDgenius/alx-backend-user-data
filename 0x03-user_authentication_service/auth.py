#!/usr/bin/env python3
"""
Module to Authenticate user
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    Hashes a password string.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a user
        """
        user = self._db._session.query(User).filter_by(email=email).first()
        if user and user.email == email:
            raise ValueError(f"User {user.email} already exists.")

        hashed_password = _hash_password(password)
        self._db.add_user(email, hashed_password=hashed_password)

        return user
