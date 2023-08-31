#!/usr/bin/env python3
""" This script contains a function to obfuscate personal data
    in log messages.
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (list of str): List of field names to be obfuscated.
        redaction (str): String to replace the field values with.
        message (str): The original log message containing the data.
        separator (str): Character used to separate fields in the message.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]*", f"{field}={redaction}",
                         message)
    return message
