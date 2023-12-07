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
        self.assertTrue(is_anagram("listen", "slient"))
        self.assertFalse(is_anagram("cheese", "liquid"))
        self.assertTrue(is_anagram("tenor", "entro"))

    def test_part3(self):
        self.assertEqual(find_primes([1, 2, 3, 4, 5]), [2, 3, 5])
        self.assertEqual(find_primes([2, 4, 6, 8, 10]), [2])
        self.assertEqual(find_primes([1, 1, 1, 1, 1, 1]), [])
        self.assertEqual(find_primes([43, 14, 83, 48, 52, 37]), [43, 83, 37])

    def test_part4(self):
        self.assertEqual(
            merge_ints([1, 2, 3, 4], [5, 6, 7, 8]), [1, 2, 3, 4, 5, 6, 7, 8]
        )
        self.assertEqual(
            merge_ints([3, 4, -1, 0], [-2, 3, 4, 5]), [-2, -1, 0, 3, 3, 4, 4, 5]
        )
        self.assertEqual(merge_ints([1, 2, 3, 4], []), [1, 2, 3, 4])
        pass


if __name__ == "__main__":
    unittest.main()
