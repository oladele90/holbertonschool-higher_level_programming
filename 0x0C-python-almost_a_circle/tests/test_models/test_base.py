#!/usr/bin/python3
"""tests for base.py"""
import unittest
from models.base import Base



class Test(unittest.TestCase):
    """unit tests"""

    def test_non(self):
        base1 = Base(None)
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)


if __name__ == '__main__':
    unittest.main()
