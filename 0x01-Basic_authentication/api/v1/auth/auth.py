#!/usr/bin/env python3
"""This module manages the API authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Provides methods for managing API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if authentication is required for a given path."""
        if path not in excluded_paths or path is None or
        excluded_paths is None or excluded_paths == []:
            return True

    def authorization_header(self, request=None) -> str:
        """Extracts the authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user based on the request."""
        return None
