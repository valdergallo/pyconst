# encoding: utf-8
from __future__ import unicode_literals, absolute_import
from .slug import slugify as s
from .slug import slugify_attr as s_attr
import enum

class PyConstString(str):

    def __new__(cls, name=None, value=None):
        if not value:
            value = name
        else:
            value = s(value)
        obj = str.__new__(cls, value)
        obj.name = name
        obj.label = name
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
        attr, value, name = (None,) * 3
        if len(iter_value) == 1:
            attr = iter_value[0]
        elif len(iter_value) == 2:
            attr, value = iter_value
        elif len(iter_value) == 3:
            attr, value, name = iter_value
        elif len(iter_value) > 3:
            name = iter_value[2]
            value = iter_value[1]
            attr = iter_value[0]
        return attr, value, name

    def to_enum(self):
        return enum.Enum('DynamicEnum', {i[0]:i[0] for i in self})

    def add(self, attr, value=None, name=None):
        "Set values in constant"

        if isinstance(attr, tuple) or isinstance(attr, list):
            attr, value, name  = self.__set_iter_value(attr)

        if attr is None:
            attr = name

        if value is None:
            value = attr

        if name is None:
            name = attr

        self.__data += (PyConstString(name=name, value=value),)
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
