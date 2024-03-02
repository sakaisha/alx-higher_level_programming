#!/usr/bin/python3
"""this is rectangle models"""

from .base import Base


class Rectangle(Base):
    """a new class named Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the attributes"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter function"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function to validate value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter function"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter function to validate value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter function"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter function to validate value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter function"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter function to validate value
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """return area of shape"""
        return self.width * self.height

    def display(self):
        """display of rectangle of # on screen"""
        print('\n' * self.y, end='')
        print((' ' * self.x + '#' * self.width + '\n') * self.height, end='')

    def __str__(self, tail=None):
        """print a str format"""
        name = self.__class__.__name__
        if tail is None:
            tail = "{}/{}".format(self.width, self.height)
        return ("[{}] ({}) {}/{} - {}".format
                (name, self.id, self.x, self.y, tail))

    def update(self, *args, **kwargs):
        """update and assign attribute"""
        key_list = ['id', 'width', 'height', 'x', 'y']
        if args is not None and args is not ():
            i = 0
            for arg in args:
                setattr(self, key_list[i], arg)
                i += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """return a dictionary type"""
        new_dict = {}
        for k, v in self.__dict__.items():
            if 'id' == k:
                new_dict['id'] = v
            elif 'width' == k[-5:]:
                new_dict['width'] = v
            elif 'height' == k[-6:]:
                new_dict['height'] = v
            elif 'x' == k[-1]:
                new_dict['x'] = v
            elif 'y' == k[-1]:
                new_dict['y'] = v
        return new_dict
