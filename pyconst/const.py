# encoding: utf-8
from __future__ import unicode_literals, absolute_import
from .slug import slugify as s
from .slug import slugify_attr as s_attr


class PyConstString(str):

    def __new__(cls, label, value):
        obj = str.__new__(cls, s(value))
        obj.label = label
        return obj


class Const(object):

    def __init__(self, *args, **kwargs):
        self.__data = ()
        for value in args:
            self.add(value)

        for label, attr in kwargs.items():
            self.add(label, attr)

    def add(self, label, attr=None, value=None):
        "Set values in constant"

        if isinstance(label, tuple) or isinstance(label, list):
            label = label[0]
            try:
                atrr = label[1]
            except IndexError:
                pass

        if not attr:
            attr = label

        if not value:
            value = attr

        self.__data += (PyConstString(label=label, value=value),)
        # set attribute as slugfiy
        self.__dict__[s_attr(attr)] = self.__data[-1]

    def __getitem__(self, index):
        "Get index item"
        return (self.__data[index], self.__data[index].label)

    def __iter__(self):
        "Lazy return"
        return ((i, i.label) for i in self.__data)

    def __len__(self):
        return len(self.__data)
