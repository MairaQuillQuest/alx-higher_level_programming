#!/usr/bin/python3
# 101-safe_function.py
# Maira Wangui

class Square:
    """ A class that defines a square by its size and position
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the square object with size and position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Method to retrieve the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Method to retrieve the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method to set the position value of the square object
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Method that returns the square area of the object
        """
        return self.__size ** 2

    def my_print(self):
        """ Method that prints the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
