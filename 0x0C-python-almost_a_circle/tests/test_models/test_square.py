#!/usr/bin/python3
"""Unittest for class base"""

import sys
import io
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """new class for square"""

    def test_1_display_10(self):
        """test display 0"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s2 = Square(2, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), "#####\n" * 5)

        """test for s2"""
        self.assertEqual(s2.__str__(), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        s2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), "  ##\n" * 2)

        """test for __str__"""
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")

        """test size"""
        self.assertEqual(s1.size, 5)

        """test when set size manually"""
        s1.size = 10
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 10")

        """test when wrong input data"""
        try:
            s1.size = "9"
        except Exception as e:
            self.assertEqual("[{}] {}".format(e.__class__.__name__, e),
                             "[TypeError] width must be an integer")

        """test when updating 10 for id"""
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 10")

        """test when update id and size"""
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")

        """test when update id, size, x"""
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")

        """test update id, size, x, y"""
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")

        """test update x by **kwargs"""
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")

        """test update size and y by **kwargs"""
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")

        """test update size and y by **kwargs"""
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")

    def test_15_ret_dict_10(self):
        """Test for new instance of Rectangle"""
        Base._Base__nb_objects = 0
        r13 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r13.__str__(), "[Rectangle] (1) 1/9 - 10/2")

    def test_16_ret_dict_11(self):
        """test return dictionary 1"""
        Base._Base__nb_objects = 0
        r13 = Rectangle(10, 2, 1, 9)
        r13_dictionary = r13.to_dictionary()
        self.assertEqual(sorted(r13_dictionary),
                         sorted({'x': 1, 'y': 9, 'id': 1, 'height': 2,
                                 'width': 10}))

    def test_17_ret_dict_12(self):
        """test return dictionary 2"""
        Base._Base__nb_objects = 0
        r13 = Rectangle(10, 2, 1, 9)
        r13_dictionary = r13.to_dictionary()
        self.assertEqual(type(r13_dictionary), dict)

    def test_18_ret_dict_13(self):
        """test return dictionary 3"""
        Base._Base__nb_objects = 0
        r23 = Rectangle(1, 1)
        self.assertEqual(r23.__str__(), "[Rectangle] (1) 0/0 - 1/1")

    def test_19_ret_dict_14(self):
        """test update instance 1"""
        Base._Base__nb_objects = 0
        r13 = Rectangle(10, 2, 1, 9)
        r23 = Rectangle(1, 1)
        r13_dictionary = r13.to_dictionary()
        r23.update(**r13_dictionary)
        self.assertEqual(r23.__str__(), "[Rectangle] (1) 1/9 - 10/2")
        self.assertFalse(r13 == r23)

    def test_21_ret_dict_16(self):
        """test update instance 2"""
        Base._Base__nb_objects = 0
        s3 = Square(10, 2, 1)
        self.assertEqual(s3.__str__(), "[Square] (1) 2/1 - 10")

    def test_22_ret_dict_17(self):
        """test update instance 3"""
        Base._Base__nb_objects = 0
        s3 = Square(10, 2, 1)
        s3_dictionary = s3.to_dictionary()
        self.assertEqual(sorted(s3_dictionary),
                         sorted({'id': 1, 'x': 2, 'size': 10, 'y': 1}))

    def test_23_ret_dict_18(self):
        """test update instance 4"""
        Base._Base__nb_objects = 0
        s3 = Square(10, 2, 1)
        s3_dictionary = s3.to_dictionary()
        self.assertEqual(type(s3_dictionary), dict)

    def test_25_ret_dict_20(self):
        """test update instance 5"""
        Base._Base__nb_objects = 0
        s3 = Square(10, 2, 1)
        s4 = Square(1, 1)
        s3_dictionary = s3.to_dictionary()
        s4.update(**s3_dictionary)
        self.assertEqual(s4.__str__(), "[Square] (1) 2/1 - 10")
        self.assertFalse(s4 == s3)

if __name__ == '__main__':
    unittest.main()
