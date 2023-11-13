#!/usr/bin/python3
""" Unittest for the Square class """
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """ Tests the square class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square(self):
        s1 = Square(5)
        self.assertEqual(s1.width + s1.height + s1.x + s1.y, 10)

    def test_size(self):
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError):
            s1.size = "9"
        self.assertEqual(s1.size, 10)

    def test_update(self):
        s1 = Square(5)

        self.assertEqual(s1.id, 1)
        s1.update(1, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)

        s1.update(1, 2, 3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)

        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

        s1.update(x=12)
        self.assertEqual(s1.x, 12)

        s1.update(size=8, y=1)
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.y, 1)

        s1.update(size=7, id=98, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 98)
        self.assertEqual(s1.y, 1)

    pass


if __name__ == "__main__":
    unittest.main()
