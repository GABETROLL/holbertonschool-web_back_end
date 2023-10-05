#!/usr/bin/env python3
"""
Learning about keeping the user's data safe
"""
from typing import List
import re
import logging


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    'message' should be similar to a CSV format:
    <field name>=<field value>{separator}<field name>=<field value>{separator}
    (I believe it should end with a separator)

    Returns 'message', but each field that has a name that's in 'fields'
    has its value replaces with 'redacion'.
    """
    result = message
    for field_name in fields:
        PATTERN = f"(?<={field_name}=)(.*?)(?={separator}$)"
        result = re.sub(PATTERN, redaction, result)
    return result


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)

        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)