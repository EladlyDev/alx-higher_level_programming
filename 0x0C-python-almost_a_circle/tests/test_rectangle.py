#!/usr/bin/python3
""" Tests the rectangle class """
from models.rectangle import Rectangle
from models.base import Base

import unittest


class TestRectangle(unittest.TestCase):
    """ Testing the rectangle class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)

    def test_init_fail(self):
        with self.assertRaises(TypeError):
            Rectangle("2", 4)
        with self.assertRaises(TypeError):
            Rectangle(4, "hi")
        with self.assertRaises(TypeError):
            Rectangle(4, 4, "hi")
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_update_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(12, 12, 12, 12, 15)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 12)
        self.assertEqual(r1.x, 12)
        self.assertEqual(r1.y, 15)

        r1.update(10)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 12)

        r1.update(1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 12)

    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)

        r1.update(width=1, x=2)
        self.assertEqual(r1.width + r1.x, 3)

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.y + r1.width + r1.x + r1.id, 95)

    def test_update_args_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(15, 20, id=12)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r1.width, 20)

        r1.update(0, id=20)
        self.assertEqual(r1.id, 0)

        with self.assertRaises(TypeError):
            r1.update(None, None, id=15)
        self.assertEqual(r1.id, None)


if __name__ == "__main__":
    unittest.main()
