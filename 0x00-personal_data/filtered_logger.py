#!/usr/bin/env python3
"""a module that substitutes log msg fields"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """a function that returns an obfuscated log message"""
    for field in fields:
        message = re.sub(field+'=.*?'+separator, field+'='+redaction, message)
    return message
