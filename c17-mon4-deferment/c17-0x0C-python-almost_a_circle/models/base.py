#!/usr/bin/python3
""" This file contains the Base class  which is the base for other classes like
rectangel, square"""
import json
import csv


class Base():
    """ The Base class
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and to
    avoid duplicating the same code (by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This method is used to initialize the instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(ld):
        """ this method converts a list of dictionaries to json str """
        if not ld:
            return "[]"
        return json.dumps(ld)

    @classmethod
    def save_to_file(cls, list_obj):
        """ this method saves a list of obj into file, as json str"""
        fname = cls.__name__ + ".json"
        out = []
        if list_obj:
            for i in list_obj:
                out.append(i.to_dictionary())
        with open(fname, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(out))

    def from_json_string(json_string):
        """ This method converts the json string into code """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ This method creates a new instance, using a **dict """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ This method loads the instance dict from the file and creates it"""
        fname = cls.__name__ + ".json"
        data = None
        try:
            with open(fname, "r", encoding="utf-8") as f:
                data = f.read()
        except FileNotFoundError:
            return []
        out = []
        items = cls.from_json_string(data)
        if items:
            for item in items:
                instance = cls.create(**item)
                out.append(instance)
        return out

    @classmethod
    def save_to_file_csv(cls, lo):
        """ This method saves list objs into csv file """
        fname = cls.__name__
        fields = lo[0].to_dictionary()
        rows = []
        for row in lo:
            out = []
            for val in row.to_dictionary():
                out.append(row.to_dictionary()[val])
            rows.append(out)
        with open(fname + ".csv", "w", encoding="utf-8") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        """ This method loads and creates list objs from csv file """
        fname = cls.__name__
        csvreader = None
        fields = []
        rows = []
        lo = []                 # list of objects
        out = []
        try:
            with open(fname + ".csv", "r", encoding='utf-8') as f:
                csvreader = csv.reader(f)
                if csvreader:
                    fields = next(csvreader)
                    for row in csvreader:
                        obj = {}
                        for key, val in enumerate(row):
                            try:
                                val = int(val)
                            except ValueError:
                                pass
                            obj.update({fields[key]: val})
                        lo.append(obj)
        except FileNotFoundError:
            return
        if lo:
            for item in lo:
                out.append(cls.create(**item))
        if out:
            return out
    pass
