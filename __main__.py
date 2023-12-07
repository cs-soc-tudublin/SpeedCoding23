import unittest

from part1 import *
from part2 import *
from part3 import *
from part4 import *


class TestFunctions(unittest.TestCase):
    def test_part1(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("ana"))
        self.assertTrue(is_palindrome("tacocat"))
        self.assertFalse(is_palindrome("cheeseburger"))
        self.assertTrue(is_palindrome("tam mat"))

    def test_part2(self):
        self.assertTrue(is_anagram("santa", "satan"))
        self.assertFalse(is_anagram("hello", "world"))

    def test_part3(self):
        pass

    def test_part4(self):
        pass


if __name__ == "__main__":
    unittest.main()
