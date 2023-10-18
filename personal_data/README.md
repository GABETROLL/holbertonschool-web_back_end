# Personal data
## Files
``user_data.csv``: User's data. Should be dumped into MySQL database.
``main.sql``: Init file for database.
``filtered_logger.py``: Helps filter the logging messages that contain PII, and returns a connection to the MySQL database.
``encrypt_password.py``: Hashes and salts passwords with ``bcrypt``. Can also verify passwords.
