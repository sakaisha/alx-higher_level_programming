#!/usr/bin/python3
"""this is base models"""

import json
import csv


class Base:
    """a new class named Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initiallize data"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        Args:
        list_dictionaries: a list of dictionaries
        """
        lis = []
        if list_dictionaries in [[None], []]:
            return "[]"
        for dictionary in list_dictionaries:
            lis += [dictionary]
        return json.dumps(lis)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file"""
        lis = []
        name = str(cls.__name__) + ".json"
        if list_objs is not None:
            for obj in list_objs:
                lis += [obj.to_dictionary()]
        with open(name, 'w') as f:
            f.write(cls.to_json_string(lis))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write a content to a file csv extension"""
        fieldnames = []
        name = str(cls.__name__) + ".csv"
        lis = []
        if list_objs is not None:
            for obj in list_objs:
                lis += [obj.to_dictionary()]
        fieldnames = sorted(list(lis[0].keys()))
        with open(name, 'w') as f:
            fwrite = csv.DictWriter(f, fieldnames=fieldnames)
            for l in lis:
                fwrite.writerow(l)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """a method to create a instance from json file"""
        name = str(cls.__name__) + ".json"
        lis = []
        new_lis = []
        try:
            with open(name, 'r') as f:
                lis = cls.from_json_string(f.read())
                for item in lis:
                    new_lis += [cls.create(**item)]
            return new_lis
        except IOError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """a method to create a instance from csv file"""
        name = str(cls.__name__) + ".csv"
        if name == "Rectangle.csv":
            fieldnames = sorted(['id', 'width', 'height', 'x', 'y'])
        else:
            fieldnames = sorted(['size', 'x', 'y', 'id'])
        new_list = []
        with open(name, 'r') as f:
            lis = csv.DictReader(f, fieldnames=fieldnames)
            for item in lis:
                temp_dic = {}
                for k, v in item.items():
                    temp_dic[k] = int(v)
                new_list += [cls.create(**temp_dic)]
        return new_list
