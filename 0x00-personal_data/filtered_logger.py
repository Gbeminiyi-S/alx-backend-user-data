#!/usr/bin/env python3
""" This script contains a function to obfuscate personal data
    in log messages.
"""

import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates specified fields in a log message."""
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]*", f"{field}={redaction}",
                         message)
    return message
