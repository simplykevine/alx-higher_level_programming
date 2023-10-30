#!/usr/bin/python3
"""calculates and return the area of the rectangle
"""

'''
File_name: 6-rectangle.py
Created: 30-OCT-2023
Author: UMUTONI Kevine (simplykevine)
Size: large
Project: 0x08-python-more_classes
Status: not yet submitted.
'''


class Rectangle:
    """
    # Write a class Rectangle that defines a rectangle by:
    # ....(based on 5-rectangle.py)
    # Instantiation with optional width and height:
    # ....def __init__(self, width=0, height=0):
    # VARIABLE(" "):
    # Rectangle_Area/Perimeter(int): String representation
    # Return: Always 0, (Success).
    """

    """ 'class rectangle' defines the class is like a blueprint or template...
    for creating objects...
    while the 'pass' is used as a placeholder when you don't want to add...
    any code in a block and this is just a sample of a 2D Polygon with a ...
    ...4-Perpendicular Sides."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ '@property' decorator allows us to retrieve the value of...
        'width' using 'rectangle_instance.width' instead of directly...
        accessing the private attribute."""
        return self.__width

    @property
    def height(self):
        """ here, we define a greater method for the private attribute...
        'height' using the '@property' decorator."""
        return self.__height

    @width.setter
    def width(self, value):
        """The setter method is called when we assign a value to...
        'rectangle_instance.width = value'.."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """inside this setter decorator, we perform the same validation...`
        as for the 'width' setter, but applied to the 'height' attribute"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ This method calculates and returns the area of the rectangle...
        which is the product of its width and height. it uses the private
        attributes'__width' and '__height' to perform the calculation"""
        return self.width * self.height

    def perimeter(self):
        """ Public instance method calculates and returns the perimeter...
        of the rectangle.. if either the width or height is equal to 0,..
        the perimeter is considered '0'. Otherwise, it calculates...
        the perimeter using the formula: 2 * (width + height).
        Again, it uses the private attributes '__width' and '__height'...
        for the calculation..."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """ '__str__()' method overrides the default string representation...
        ...of the object when using 'str(rectangle_instance)'....
        it creates a string representation of the triangle using the '#'..."""
        """if either the width or height is equal to '0' or an empty....
            string is returned.. It uses a 'Loop' to build the string...
            representation by concatenating the appropriate number of '#'...
            characters for each row.."""
        if self.width == 0 or self.height == 0:
            return ''
        else:
            res = list(map(
                lambda x: '#' * self.width + '\n' * (x != self.height - 1),
                range(self.height)))
            return ''.join(res)

    def __repr__(self):
        """This method returns a string representation of the object...
        that can be used to recreate a new instance of the 'Rectangle class"""
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        """'number_of_instances' class is a public class attribute that keeps
        track of the number of 'Rectangle' instances...It is initialized to..
        '0' and is incremented during each new instance instantiation"""
        """ It is decremented during each instance deletion"""
        """'__del__() method is called when an instance of the 'Rectangle'...
        class is Deleted... Then it Prints  the Message...'Bye Rectangle'..
        ...to indicate that the instance is been Deleted."""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
