#!/usr/bin/python3
"""Unittest for Rectangle"""

import sys
import io
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """new class Rectangle"""

    def test_0_set_id(self):
        """test id first"""
        Base._Base__nb_objects = 0
        r12 = Rectangle(10, 2)
        r22 = Rectangle(10, 2, 0, 0, 3)
        r32 = Rectangle(2, 10)
        self.assertEqual(r12.id, 1)
        self.assertEqual(r22.id, 3)
        self.assertEqual(r32.id, 2)

    def test_1_data_check_0(self):
        """test for wrong input data 1"""
        try:
            Rectangle(10, "2")
        except Exception as e:
            self.assertEqual("[{}] {}".format(e.__class__.__name__, e),
                             "[TypeError] height must be an integer")

    def test_2_data_check_1(self):
        """test for wrong input data 2"""
        try:
            r = Rectangle(10, 2)
            r.width = -10
        except Exception as e:
            self.assertEqual("[{}] {}".format(e.__class__.__name__, e),
                             "[ValueError] width must be > 0")

    def test_3_data_check_2(self):
        """test for wrong input data 3"""
        try:
            r = Rectangle(10, 2)
            r.x = {}
        except Exception as e:
            self.assertEqual("[{}] {}".format(e.__class__.__name__, e),
                             "[TypeError] x must be an integer")

    def test_4_data_check_3(self):
        """test for wrong input data 4"""
        try:
            Rectangle(10, 2, 3, -1)
        except Exception as e:
            self.assertEqual("[{}] {}".format(e.__class__.__name__, e),
                             "[ValueError] y must be >= 0")

    def test__5_area_0(self):
        """test for area method 1"""
        Base._Base__nb_objects = 0
        r42 = Rectangle(3, 2)
        self.assertEqual(r42.area(), 6)

    def test__6_area_1(self):
        """test for area method 2"""
        Base._Base__nb_objects = 0
        r52 = Rectangle(2, 10)
        self.assertEqual(r52.area(), 20)

    def test__7_area_3(self):
        """test for area method 3"""
        Base._Base__nb_objects = 0
        r62 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r62.area(), 56)

    def test_8_display_0(self):
        """test output"""
        Base._Base__nb_objects = 0
        r72 = Rectangle(4, 6)
        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        r72.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), "####\n" * 6)

    def test_9__str__0(self):
        """test str method 1"""
        Base._Base__nb_objects = 0
        r82 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r82.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_10__str__1(self):
        """test str method 2"""
        Base._Base__nb_objects = 0
        r92 = Rectangle(5, 5, 1)
        self.assertEqual(r92.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    def test_11_display_1(self):
        """test output 1"""
        Base._Base__nb_objects = 0
        r102 = Rectangle(2, 3, 2, 2)
        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        r102.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), ("\n\n" + "  ##\n" * 3))

    def test_12_update_0(self):
        """test udpate 0"""
        Base._Base__nb_objects = 0
        r112 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r112.__str__(), "[Rectangle] (1) 10/10 - 10/10")

    def test_13_update_1(self):
        """test udpate 1"""
        Base._Base__nb_objects = 0
        r112 = Rectangle(10, 10, 10, 10)
        r112.update(89)
        self.assertEqual(r112.__str__(), "[Rectangle] (89) 10/10 - 10/10")

    def test_14_update_2(self):
        """test udpate 2"""
        Base._Base__nb_objects = 0
        r112 = Rectangle(10, 10, 10, 10)
        r112.update(89)
        r112.update(89, 2)
        self.assertEqual(r112.__str__(), "[Rectangle] (89) 10/10 - 2/10")

    def test_15_update_3(self):
        """test udpate 3"""
        Base._Base__nb_objects = 0
        r112 = Rectangle(10, 10, 10, 10)
        r112.update(89)
        r112.update(89, 2)
        r112.update(89, 2, 3)
        self.assertEqual(r112.__str__(), "[Rectangle] (89) 10/10 - 2/3")

    def test_16_update_4(self):
        """test udpate 4"""
        Base._Base__nb_objects = 0
        r112 = Rectangle(10, 10, 10, 10)
        r112.update(89)
        r112.update(89, 2)
        r112.update(89, 2, 3)
        r112.update(89, 2, 3, 4)
        self.assertEqual(r112.__str__(), "[Rectangle] (89) 4/10 - 2/3")

    def test_17_update_5(self):
        """test udpate 5"""
        Base._Base__nb_objects = 0
        r112 = Rectangle(10, 10, 10, 10)
        r112.update(89)
        r112.update(89, 2)
        r112.update(89, 2, 3)
        r112.update(89, 2, 3, 4)
        r112.update(89, 2, 3, 4, 5)
        self.assertEqual(r112.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_18_update_6(self):
        """test udpate 6"""
        Base._Base__nb_objects = 0
        r122 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r122.__str__(), "[Rectangle] (1) 10/10 - 10/10")

    def test_19_update_11(self):
        """test udpate 7"""
        Base._Base__nb_objects = 0
        r122 = Rectangle(10, 10, 10, 10)
        r122.update(height=1)
        self.assertEqual(r122.__str__(), "[Rectangle] (1) 10/10 - 10/1")

    def test_20_update_12(self):
        """test udpate 8"""
        Base._Base__nb_objects = 0
        r122 = Rectangle(10, 10, 10, 10)
        r122.update(height=1)
        r122.update(width=1, x=2)
        self.assertEqual(r122.__str__(), "[Rectangle] (1) 2/10 - 1/1")

    def test_21_update_13(self):
        """test udpate 9"""
        Base._Base__nb_objects = 0
        r122 = Rectangle(10, 10, 10, 10)
        r122.update(height=1)
        r122.update(width=1, x=2)
        r122.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r122.__str__(), "[Rectangle] (89) 3/1 - 2/1")

    def test_22_update_14(self):
        """test udpate 10"""
        Base._Base__nb_objects = 0
        r122 = Rectangle(10, 10, 10, 10)
        r122.update(height=1)
        r122.update(width=1, x=2)
        r122.update(y=1, width=2, x=3, id=89)
        r122.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r122.__str__(), "[Rectangle] (89) 1/3 - 4/2")

if __name__ == '__main__':
    unittest.main()
