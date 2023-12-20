#!/usr/bin/python3
"""class Square that defines a square by: (based on 0-square.py)
attribute:
    size: size of  square(1 side)
    """


class Square:
    """Creates new instances of square (1 side).

        Args:
            size: size of the square.
        """
    def __init__(self, size):
        self.__size = size
