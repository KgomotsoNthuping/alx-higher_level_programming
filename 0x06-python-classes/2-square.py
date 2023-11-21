!/usr/bin/python3

"""define square"""


class Square:
    """ a square
    Attributes:
        ___size (int): one side
    """
    def __init__(self, size=0):
        """Initialise square
        Args:
            size (int): one side
        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
