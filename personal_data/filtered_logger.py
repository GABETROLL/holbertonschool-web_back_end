#!/usr/bin/env python3
"""
Learning about keeping the user's data safe
"""
from typing import List
import re


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
    return separator.join(
        re.sub(f"(?<==)(.*?)(?={separator})", redaction, field)
        if field.split("=")[0] in fields
        else field
        for field in message.split(separator)
    )
