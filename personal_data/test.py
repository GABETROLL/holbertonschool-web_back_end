#!/usr/bin/env python3
"""
Main file
"""
import unittest
import random
from filtered_logger import filter_datum

FIELDS = ["password", "date_of_birth"]
REDACTION = "xxx"


class Main(unittest.TestCase):
    def test_filter_datum(self):

        for separator_ord in range(33, 126 + 1):
            separator = chr(separator_ord)

            for c1 in range(33, 126 + 1):
                for c2 in range(33, 126 + 1):

                    password = chr(c1) + chr(c2)

                    self.assertEqual(
                        filter_datum(FIELDS, REDACTION, f"password={password}{separator}", separator),
                        f"password={REDACTION}{separator}",
                        msg=f"FAILURE: {separator=} {password=}"
                    )
            
            for a in range(31 + 1):
                for b in range(31 + 1):
                    for year in range(2023):
                        date_of_birth = f"{a}/{b}/{year}"

                        self.assertEqual(
                            filter_datum(FIELDS, REDACTION, f"date_of_birth={date_of_birth}{separator}", separator),
                            f"date_of_birth={REDACTION}{separator}",
                            msg=f"FAILURE: {separator=} {date_of_birth=}"
                        )