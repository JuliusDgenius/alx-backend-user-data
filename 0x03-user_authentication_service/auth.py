#!/usr/bin/env python3
"""
Module to Authenticate user
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password string.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
