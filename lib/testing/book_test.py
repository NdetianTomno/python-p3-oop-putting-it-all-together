#!/usr/bin/env python3

from book import Book

import unittest
import sys
import io
from book import Book

class TestBook(unittest.TestCase):
    def test_title_string(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            Book(title=123, page_count=100)
        except ValueError as e:
            self.assertEqual(str(e), "Title must be a string.")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "")

    def test_page_count_not_integer(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            Book(title="Title", page_count="100")
        except ValueError as e:
            self.assertEqual(str(e), "Page count must be an integer.")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
