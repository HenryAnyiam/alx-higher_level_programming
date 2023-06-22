#!/usr/bin/python3

"""base module with Base class"""

import json
import csv


class Base:
    """building class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of Base class

        Args:
            id

        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns serialized representation of list_dictionaries"""

        if list_dictionaries is None:
            return str([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saved the serialized representation of class instance to file"""

        obj = []
        if list_objs is not None and isinstance(list_objs, list):
            for i in list_objs:
                obj.append(i.to_dictionary())
        objs = Base.to_json_string(obj)
        with open(f"{cls.__name__}.json", "w", encoding="UTF-8") as MyFile:
            MyFile.write(objs)

    @staticmethod
    def from_json_string(json_string):
        """returns the desiarilzed representation of json_string"""

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a new class instance with given **kwargs"""

        if (cls.__name__ == "Square"):
            dummy = cls(3)
        else:
            dummy = cls(3, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """loads a new class instance from saved file"""

        try:
            MyFile = open(f"{cls.__name__}.json", encoding="UTF-8")
        except FileNotFoundError:
            return None
        else:
            obj = []
            for line in MyFile:
                obj = cls.from_json_string(line)
            objs = []
            for i in obj:
                objs.append(cls.create(**i))
            return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        data = []
        if list_objs is not None and isinstance(list_objs, list):
            for i in list_objs:
                data.append(i.to_dictionary())
        save_data = []
        for i in data:
            save_data.append(list(i.values()))
        with open(f"{cls.__name__}.csv", "w", encoding="UTF-8") as MyFile:
            obj = csv.writer(MyFile)
            obj.writerows(save_data)

    @classmethod
    def load_from_file_csv(cls):
        data = []
        with open(f"{cls.__name__}.csv", encoding="UTF-8") as MyFile:
            obj = csv.reader(MyFile)
            for line in obj:
                data.append(line)
        objs = []
        for i in data:
            load_data = {}
            load_data["id"] = int(i[0])
            load_data["x"] = int(i[-2])
            load_data["y"] = int(i[-1])
            if cls.__name__ == "Square":
                load_data["size"] = int(i[1])
            else:
                load_data["width"] = int(i[1])
                load_data["height"] = int(i[2])
            objs.append(cls.create(**load_data))
        return objs
