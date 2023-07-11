#!/usr/bin/python3

""" json """


class Student:
    """ Class Student """

    def __init__(self, first_name, last_name, age):
        """ Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves Class dictionary base on attr
        """
        if not isinstance(attrs, list) or \
           not all(isinstance(k, str) for k in attrs):

            dic = self.__dict__.copy()
        else:

            dic = {k: self.__dict__[k] for k in attrs if k in self.__dict__}

        return dic

    def reload_from_json(self, json):
        """ replaces attributes of the Student instance """
        for k in json:
            self.__dict__[k] = json[k]
