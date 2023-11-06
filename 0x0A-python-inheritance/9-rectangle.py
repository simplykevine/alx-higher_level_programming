#!/usr/bin/python3
'''Class Rectangle that inherits from BaseGeometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class that inherits the BaseGeometry '''

    def __init__(self, width, height):
        '''A function that created a rectangle '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        '''Function to return the area of the rectangle'''
        return self.__height * self.__width

    def __str__(self):
        '''"Return the print() and str() representation of a Rectangle '''
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
