#!/usr/bin/python3

"""9-student module with Student class"""


class Student:
    """defines a simple student class"""

    def __init__(self, first_name, last_name, age):
        """initialization of class Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representatio"""

        return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
