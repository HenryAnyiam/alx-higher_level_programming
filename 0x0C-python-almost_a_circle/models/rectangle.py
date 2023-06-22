#!/usr/bin/python3

"""recatangle module with class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """building new class inheriting from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of class Rectangle

        Args:
            width: width of rectangle class instance
            height; height of rectangle class instance
            x: x coordinate
            y: y coordinaate
            id

        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        Base.__init__(self, id)

    @property
    def width(self):
        """gets private attribute width

        setter ensures width is greater than 0

        """

        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets private attribute height

        setter ensures height is greater than 0

        """

        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets private attribute x

        setter ensures x is greater than or
        equal to 0

        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets private attribute y

        setter ensures y is greater than or
        equal to 0

        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """gets the area of rectangle class instance"""

        return self.__width * self.__height

    def display(self):
        """prints out the class instance with #"""

        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, "#" * self.__width, sep="")

    def __str__(self):
        """returns the string representation of the class instance"""

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "\
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """update the class instance with given arguments

        Args:
            *args
            **kwargs

        """

        length = len(args)
        if length > 0:
            self.id = args[0]
        if length > 1:
            self.__width = args[1]
        if length > 2:
            self.__height = args[2]
        if length > 3:
            self.__x = args[3]
        if length > 4:
            self.__y = args[4]
        if length == 0 and "width" in kwargs:
            self.__width = kwargs["width"]
        if length == 0 and "id" in kwargs:
            self.id = kwargs["id"]
        if length == 0 and "height" in kwargs:
            self.__height = kwargs["height"]
        if length == 0 and "x" in kwargs:
            self.__x = kwargs["x"]
        if length == 0 and "y" in kwargs:
            self.__y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of class instance"""

        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
