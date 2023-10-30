#!/usr/bin/python3
""" calculates and return the area of the rectangle
"""

'''
File_name: 2-rectangle.py
Created: 30-OCT-2023
Author:UMUTONI Kevine (simplykevine)
Size: large
Project: 0x08-python-more_classes
Status: not yet submitted
'''


class Rectangle:
    """
    # Write a class Rectangle that defines a rectangle by:
    # ....(based on 1-rectangle.py)
    # Instantiation with optional width and height:
    # ....def __init__(self, width=0, height=0):
    # VARIABLE(" "):
    # Rectangle_Area/Perimeter(int): Area and Perimeter
    # Return: Always 0, (Success).
    """

    """ 'class rectangle' defines the class is like a blueprint or template...
    for creating objects...
    while the 'pass' is used as a placeholder when you don't want to add...
    any code in a block and this is just a sample of a 2D Polygon with a ...
    ...4-Perpendicular Sides."""
    def __init__(self, width=0, height=0):
        """
        initializes rectangle

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ '@property' decorator allows us to retrieve the value of...
        'width' using 'rectangle_instance.width' instead of directly...
        accessing the private attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter method is called when we assign a value to...
        'rectangle_instance.width = value'.."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ here, we define a greater method for the private attribute...
        'height' using the '@property' decorator."""
        return self.__height

    @height.setter
    def height(self, value):
        """inside this setter decorator, we perform the same validation...`
        as for the 'width' setter, but applied to the 'height' attribute"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ This method calculates and returns the area of the rectangle...
        which is the product of its width and height. it uses the private
        attributes'__width' and '__height' to perform the calculation"""
        return self.__width * self.__height

    def perimeter(self):
        """ Public instance method calculates and returns the perimeter...
        of the rectangle.. if either the width or height is equal to 0,..
        the perimeter is considered '0'. Otherwise, it calculates...
        the perimeter using the formula: 2 * (width + height).
        Again, it uses the private attributes '__width' and '__height'...
        for the calculation..."""
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)
