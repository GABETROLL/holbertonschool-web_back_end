#!/usr/bin/env python3
"""
Learning about keeping the user's data safe.

This file is meant to be run in a server.
"""
from typing import List
import re
import logging
from os import environ
import mysql.connector

PII_FIELDS = "email", "name", "ssn", "password", "phone"


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
        PATTERN = f"(?<={field_name}=)(.*?)(?={separator})"
        result = re.sub(PATTERN, redaction, result)
    return result


class RedactingFormatter(logging.Formatter):
    """
    Uses 'filter_datum' to redact the PII fields
    in a record message.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)

        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Returns the 'record.getMessage()',
        formatted using '% self.FORMAT',
        and filtered to censor the sensitive user information,
        using the 'filter_datum' function,
        """
        FORMATTED_MSG: str = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, FORMATTED_MSG, self.SEPARATOR
        )


def get_logger() -> logging.Logger:
    """
    Returns a new 'logging.Logger' instance.

    The instance has a level of 'logging.INFO',
    doesn't propagate to other 'logging.Logger' objects,
    and has a 'StreamHandler' that has a 'RedactingFormatter'
    as its 'logging.Formatter'.
    """
    result: logging.Logger = logging.getLogger("user_data")

    result.setLevel(logging.INFO)
    result.propagate = False

    HANDLER: logging.StreamHandler = logging.StreamHandler()

    HANDLER.setFormatter(RedactingFormatter(PII_FIELDS))

    result.addHandler(HANDLER)

    return result


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Using environment variables
    'PERSONAL_DATA_DB_USERNAME',
    'PERSONAL_DATA_DB_PASSWORD',
    'PERSONAL_DATA_DB_HOST' and
    'PERSONAL_DATA_DB_NAME',

    this function returns a MySQL connector
    for the database containing the PII.
    """
    return mysql.connector.connect(
        user=environ.get("PERSONAL_DATA_DB_USERNAME"),
        password=environ.get("PERSONAL_DATA_DB_PASSWORD"),
        host=environ.get("PERSONAL_DATA_DB_HOST"),
        database=environ.get("PERSONAL_DATA_DB_NAME")
    )


def main() -> None:
    """
    Displays all of the rows of user's data in
    this server's database, through 'get_db()',

    using the logger in returned by 'get_logger()',
    to hide the PII (name, email, phone, ssn, password)
    """
    LOGGER: logging.Logger = get_logger()

    DB = get_db()
    DB_CURSOR = DB.cursor()

    DB_CURSOR.execute(
        "SELECT"
        "name, email, phone, ssn, password, ip, last_login, user_agent"
        "FROM USERS"
    )

    for (
            name,
            email,
            phone,
            ssn,
            password,
            ip,
            last_login,
            user_agent) in DB_CURSOR:
        LOGGER.log(
            logging.INFO,
            f"{name=}{RedactingFormatter.SEPARATOR}"
            f"{email=}{RedactingFormatter.SEPARATOR}"
            f"{phone=}{RedactingFormatter.SEPARATOR}"
            f"{ssn=}{RedactingFormatter.SEPARATOR}"
            f"{password=}{RedactingFormatter.SEPARATOR}"
            f"{ip=}{RedactingFormatter.SEPARATOR}"
            f"{last_login=}{RedactingFormatter.SEPARATOR}"
            f"{user_agent=}{RedactingFormatter.SEPARATOR}"
        )


if __name__ == '__main__':
    main()
