#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -20, -3, -100]), -3)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 2, 99, -100]), 99)

    def test_all_same(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        self.assertEqual(max_integer([1.2, 3.5, 2.4]), 3.5)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "b", "z"]), "z")

    def test_string_input(self):
        self.assertEqual(max_integer("abcde"), "e")

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_iterable(self):
        with self.assertRaises(TypeError):
            max_integer(123)


if __name__ == "__main__":
    unittest.main()
