#!/usr/bin/python3i
"""calculates and return the area of the rectangle
"""

'''
File_name: 8-rectangle.py
Created: 30-OCT-2023
Author: UMUTONI Kevine (simplykevine)
Size: Large
Project: 0x08-python-more_classes
Status: not yet submitted.

'''


class Rectangle:
    """
    # Write a class Rectangle that defines a rectangle by:
    # ....(based on 7-rectangle.py)
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
    """ The '__str__(0' method provides a string representation of the...
    rectangle using the 'print_symbol', and the '__repr__()' method...
    returns a string representation that can be used to....
    recreate a new instance using 'eval()"""
    """ rectangle with private instance attributes width and height """
    """ The '__str__(0' method provides a string representation of the...
    rectangle using the 'print_symbol', and the '__repr__()' method...
    returns a string representation that can be used to....
    recreate a new instance using 'eval()"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializes rectangle

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

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
        if value < 0:
            raise ValueError('width must be >= 0')
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
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ This method calculates and returns the area of the rectangle...
        which is the product of its width and height. it uses the private
        attributes'__width' and '__height' to perform the calculation"""
        return self.width * self.height

    def perimeter(self):
        """ This method calculates and returns the area of the rectangle...
        which is the product of its width and height. it uses the private
        attributes'__width' and '__height' to perform the calculation"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ '__str__()' method overrides the default string representation...
        ...of the object when using 'str(rectangle_instance)'....
        it creates a string representation of the triangle using the '#'..."""
        """if either the width or height is equal to '0' or an empty....
            string is returned.. It uses a 'Loop' to build the string...
            representation by concatenating the appropriate number of '#'...
            characters for each row.."""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            string += str(self.print_symbol) * self.width
            if i < self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """This method returns a string representation of the object...
        that can be used to recreate a new instance of the 'Rectangle class"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """'number_of_instances' class is a public class attribute....
         that track of the number of 'Rectangle' instances
         ...It is initialized to..
        '0' and is incremented during each new instance instantiation"""
        """ It is decremented during each instance deletion"""
        """'__del__() method is called when an instance of the 'Rectangle'...
        class is Deleted... Then it Prints  the Message...'Bye Rectangle'..
        ...to indicate that the instance is been Deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns rectangle with largest area """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
