#!/usr/bin/python3

"""9-student module with Student class"""


class Student:
    """defines a simple student class"""

    def __init__(self, first_name, last_name, age):
        """initialization of class Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representatio"""
        if attrs is None:
            return {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age
                    }
        dic = {}
        if "first_name" in attrs:
            dic["first_name"] = self.first_name
        if "last_name" in attrs:
            dic["last_name"] = self.last_name
        if "age" in attrs:
            dic["age"] = self.age
        return dic

    def reload_from_json(self, json):
        """replaces attributes of student instance"""

        if "first_name" in json:
            self.first_name = json["first_name"]
        if "last_name" in json:
            self.last_name = json["last_name"]
        if "age" in json:
            self.age = json["age"]
