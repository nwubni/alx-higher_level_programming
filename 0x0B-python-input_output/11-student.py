#!/usr/bin/python3

"""Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Class initializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary description of object"""
        if (type(attrs) == list and all(isinstance(item, (str)) for item in attrs)):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

        return self.__dict__

    def reload_from_json(self, json):
        """Reloads from json"""
        for key, value in json.items():
            setattr(self, key, value)
