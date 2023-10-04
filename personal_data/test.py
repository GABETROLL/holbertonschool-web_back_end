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

        for c1 in range(33, 126 + 1):
            for c2 in range(33, 126 + 1):

                password = chr(c1) + chr(c2)

                self.assertEqual(
                    filter_datum(fields, "xxx", f"password={password};", ';'),
                    "password=xxx;",
                    msg=f"FAILURE: {password}"
                )