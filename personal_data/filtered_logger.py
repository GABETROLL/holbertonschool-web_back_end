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
        # print(f"BEFORE: {PATTERN = }; {field_name = }; {result = }")
        result = re.sub(PATTERN, redaction, result)
        # print(f"AFTER: {PATTERN = }; {field_name = }; {result = }")        
    return result