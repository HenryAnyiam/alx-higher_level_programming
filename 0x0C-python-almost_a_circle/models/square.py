#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """initialization of class Square

        Args:
            size: width & height
            x: x coordinate
            y: y coordinate
            id: id

        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns the string representation of the class instance"""

        return f"[Square] ({self.id}) {super().x}/{super().y} - "\
            f"{super().width}"

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

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
            self.size = args[1]
        if length > 2:
            self.x = args[2]
        if length > 3:
            self.y = args[3]
        if length == 0 and "size" in kwargs:
            self.size = kwargs["size"]
        if length == 0 and "id" in kwargs:
            self.id = kwargs["id"]
        if length == 0 and "x" in kwargs:
            self.x = kwargs["x"]
        if length == 0 and "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of class instance"""

        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
