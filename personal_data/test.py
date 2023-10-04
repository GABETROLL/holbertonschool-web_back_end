#!/usr/bin/env python3
"""
Main file
"""
import unittest
import random

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]


class Main(unittest.TestCase):
    def test_filter_datum(self):

        for password_ord in range(33, 126 + 1):
            password = chr(password_ord)

            self.assertEqual(
                filter_datum(fields, "xxx", f"password={password};", ';'),
                "password=xxx;",
                msg=f"FAILURE: {password}"
            )