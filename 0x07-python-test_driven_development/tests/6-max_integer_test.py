#!/usr/bin/python3
""" A unittest for the ``max_integer`` function """

import unittest
mi = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """ This is a test case for the function ``max_integer`` """

    def test_basic(self):
        self.assertEqual(mi([1, 2, 3, 4]), 4)
        self.assertEqual(mi([1, 3, 4, 2]), 4)
        self.assertIsNone(mi([]))
        self.assertEqual(mi([1]), 1)
        self.assertEqual(mi([0, 1]), 1)
        self.assertEqual(mi([[1, 2, 3], [4, 5, 6]]), [4, 5, 6])
        self.assertTrue(mi([True, False]))
        self.assertEqual(mi(["a", "b"]), "b")
        self.assertEqual(mi(["1234", "5678"]), "5678")
        self.assertEqual(mi([-99, -1]), -1)
        self.assertIsNone(mi([None]))
        self.assertEqual(mi("hi"), "i")
        self.assertEqual(mi(("1", "2")), "2")
