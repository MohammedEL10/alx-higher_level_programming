#!/usr/bin/python3
class Reactangle:
    """A Rectangle with a width and height."""
    def __int__(self, w, h):
        """ (Rectangle, number, number)
        Create a new rectange of width w and height h.

        >>> r = Rectangle(1, 2)
        >>> r.width
        1
        >>> r.height
        2
        """
        self.width = w
        self.height = h
        def area(self):
            """(Rectangle) ->number
            Return the area of this rectangle.
            >>> r = Rectangle(10, 20)
            >>> r.area()
            200
            """

            return self.width * self.height

