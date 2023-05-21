#!/usr/bin/env python3

from shoe import Shoe

import unittest
import sys
import io
from shoe import Shoe

class TestShoe(unittest.TestCase):
    def test_brand_string(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            Shoe(brand=123, size=9)
        except ValueError as e:
            self.assertEqual(str(e), "Brand must be a string.")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "")

    def test_size_not_integer(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            Shoe(brand="Brand", size="9")
        except ValueError as e:
            self.assertEqual(str(e), "Size must be an integer.")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "")

    def test_repair_shoe(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        shoe = Shoe(brand="Brand", size=9)
        shoe.repair()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "The shoe has been repaired.\n")
        self.assertEqual(shoe.condition, "New")


if __name__ == "__main__":
    unittest.main()
