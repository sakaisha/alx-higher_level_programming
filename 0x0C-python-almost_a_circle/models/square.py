#!/usr/bin/python3
"""square models"""

from .rectangle import Rectangle


class Square(Rectangle):
    """new Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """inherit form Rectangle and initialize data"""
        Rectangle.__init__(self, size, size, x=x, y=y, id=id)

    @property
    def size(self):
        """getter function"""
        return self.width

    @size.setter
    def size(self, size):
        """setter function"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size
            self.height = size

    def __str__(self):
        """overide the Rectangle class"""
        tail = "{}".format(self.width)
        return Rectangle.__str__(self, tail)

    def update(self, *args, **kwargs):
        """update attribute"""
        key_list = ['id', 'size', 'x', 'y']
        if args != ():
            i = 0
            for arg in args:
                setattr(self, key_list[i], arg)
                i += 1
        elif kwargs != {}:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """return dictionary representation of a object"""
        new_dict = {}
        for k, v in self.__dict__.items():
            if 'width' == k[-5:] or 'height' == k[-6:]:
                new_dict['size'] = v
            elif 'id' == k:
                new_dict['id'] = v
            elif 'x' == k[-1]:
                new_dict['x'] = v
            elif 'y' == k[-1]:
                new_dict['y'] = v
        return new_dict
