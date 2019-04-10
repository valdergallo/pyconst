# encoding: utf-8
from __future__ import unicode_literals, absolute_import
from .slug import slugify as s
from .slug import slugify_attr as s_attr
import enum

class PyConstString(str):

    def __new__(cls, name=None, value=None, to_case='upper'):
        if not value:
            value = name
        if to_case == 'upper':
            value = s(value).upper()
        elif to_case == 'lower':
            value = s(value).lower()
        else:
            value = s(value)
        obj = str.__new__(cls, value)
        obj.name = name
        obj.value = value
        return obj


class Const(object):

    def __init__(self, *args, **kwargs):
        self.__data = ()
        for value in args:
            self.add(value)

        for name, attr in kwargs.items():
            self.add(name, attr)

    def __set_iter_value(self, iter_value):
        name, attr, value = (None,) * 3
        if len(iter_value) == 1:
            name = iter_value[0]
        elif len(iter_value) == 2:
            name, attr = iter_value
        elif len(iter_value) == 3:
            name, attr, value = iter_value
        elif len(iter_value) > 3:
            attr = iter_value[1]
            value = iter_value[2]
            name = iter_value[0]
        return name, attr, value

    def get_const_string(self, name, value):
        return PyConstString(name=name, value=value, to_case="upper")

    def to_enum(self):
        return enum.Enum('DynamicEnum', {i[0]:i[0] for i in self})

    def add(self, name, attr=None, value=None):
        "Set values in constant"

        if isinstance(name, tuple) or isinstance(name, list):
            name, attr, value = self.__set_iter_value(name)

        if attr is None:
            attr = name

        if value is None:
            value = attr

        self.__data += (self.get_const_string(name=name, value=value),)
        # set attribute as slugfiy
        self.__dict__[s_attr(attr)] = self.__data[-1]

    def __getitem__(self, index):
        "Get index item"
        return (self.__data[index], self.__data[index].name)

    def __iter__(self):
        "Lazy return"
        return ((i, i.name) for i in self.__data)

    def __len__(self):
        return len(self.__data)


class LowerConst(Const):
    "Force value to lower case by default"

    def get_const_string(self, name, value):
        return PyConstString(name=name, value=value, to_case="lower")


class UpperConst(Const):
    "Force value to upper case"

    def get_const_string(self, name, value):
        return PyConstString(name=name, value=value, to_case="upper")


class DefaultConst(Const):
    "Default value with only using slugify"

    def get_const_string(self, name, value):
        return PyConstString(name=name, value=value, to_case=None)
